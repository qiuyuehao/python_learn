#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from qyh_stock import Ui_MainWindow
from search_stock_name import get_stock_num_by_name
from get_dfcfgupiao import get_gupiao_info
import sys, time, threading
import urllib.request
from PyQt5.QtWidgets import *
from send_mail import send_mail_to_myself
from send_wechat_msg import send_wechat_msg_to_myself
from monitor_gupiao import compare_gupiao_info_from_file
import os, re


zs_list=['000001', '399001', '399006']
notify_method = "mail"
notify_time = 60 * 30
class MyWidgets(QWidget):
	msec = 1000
	pre_date_day = 0;
	running_cnt = 0
	stock_notify_already = {}
	debug = False
	def __init__(self):
		super().__init__()
		self.__ui=Ui_MainWindow()
		self.__ui.setupUi(self)
		self.__ui.pushButton_2.clicked.connect(self.close)
		self.__ui.pushButton.clicked.connect(self.start)
		t = threading.Thread(target=compare_gupiao_info_from_file)
		t.start()
		self.get_and_update_init_stock_info()
		try:
			self.start_get_zs_info()
			self.start_get_info()
		except:
			print("init start fail")
		self.start()
	def get_zs_name(self, zs_str):
		if zs_str == "000001":
			return str("上证指数")
		elif zs_str == "399001":
			return str("深证指数")
		elif zs_str == "399006":
			return str("创业板")
		else:
			return str("未知指数")
	def close(self):
		os.system('killall -9 qyh_stock_main_for_dfcf.py')
	def update_notify_value(self, name):
		print("call update_notify_value name", name)
		self.stock_notify_already[name] = 0
	def notify_user_message(self, name, up_down_value, other_info, method):
		if self.is_deal_time_now() == False:
			return
		if self.stock_notify_already[name] == 0:
			print("not notify yet")
			new_timer_thread = threading.Timer(notify_time, self.update_notify_value, (name,)).start()
			self.stock_notify_already[name] = 1
		else:
			method = None
		if up_down_value > 0:
			tmp_content = name + "good news  +++  " + str(up_down_value) + "   price information:" +str(other_info)
		else:
			tmp_content = name + "bad news  --- " + str(up_down_value) + "   price information:" +str(other_info)
		if method == "wechat":
			send_wechat_msg_to_myself(tmp_content)
		elif method == "mail":
			send_mail_to_myself(tmp_content, "no content")
		else:
			print(tmp_content)
	def start_get_zs_info(self):
		#print(len(zs_list))
		cnt = 0
		zs_info_list = []
		with open("zs_pool.txt", "r") as f:
			for number, line in enumerate(f,start=1):
				line = line.strip('\n').strip('\r')
				if line != None:
					line = re.sub(' +', ' ', line)
					line_info = line.split(" ")
				name = line_info[0]
				return_value = get_gupiao_info(name)
				if return_value != None:
					(prePrice, price, time) = return_value
					prePrice = float(prePrice)
					price = float(price)
					if price - prePrice > 0:
						up_down_percent = str((price -prePrice) / prePrice * 100 + 0.005)[0:4]
					else:
						up_down_percent = str((price -prePrice) / prePrice * 100 - 0.005)[0:5]

					up_down_value = str(price - prePrice)
					value = str(price)
					up_down_percent_result = up_down_percent + '%'
					zs_stock_info = {}

					zs_stock_info["stock_name"] = self.get_zs_name(name)
					zs_stock_info["value"] = value
					zs_stock_info["up_down_percent"] = up_down_percent_result
					zs_info_list.append(zs_stock_info)
					if zs_stock_info["stock_name"] in self.stock_notify_already.keys():
						pass
					else:
						self.stock_notify_already[zs_stock_info["stock_name"]] = 0
					float_up_down = float(up_down_percent)
					notify = str(self.__ui.get_zs_notify_value(cnt))
					limit = str(self.__ui.get_zs_limit_value(cnt))
					cnt = cnt + 1
					try:
						notify = float(notify)
						limit = float(limit)
					except:
						continue
					if (abs(float_up_down) > abs(limit)) and (notify == 1) and (limit != 0):
						self.notify_user_message(zs_stock_info["stock_name"], float_up_down, limit, notify_method)
		self.__ui.update_zs_stock_info(zs_info_list)
	def get_and_update_init_stock_info(self):
		stock_list = []
		with open("stock_pool.txt", "r") as f:
			for number, line in enumerate(f,start=1):
				line = line.strip('\n').strip('\r')
				if line != None:
					line = re.sub(' +', ' ', line)
					line_info = line.split(" ")
				name = line_info[0]
				stock_list_dict = {}
				stock_list_dict["stock_name"] = name
				stock_list_dict["up_down_percent"] = "unknow"
				stock_list_dict["up_down_value"] = "unknow"
				stock_list_dict["value"] = "unknow"
				if len(line_info) == 2:
					stock_list_dict["notify"] = "1"
					stock_list_dict["limit"] = line_info[1]
				if len(line_info) == 3:
					stock_list_dict["notify"] = "1"
					stock_list_dict["limit"] = line_info[1]
					stock_list_dict["upper"] = line_info[2]
				if len(line_info) == 4:
					stock_list_dict["notify"] = "1"
					stock_list_dict["limit"] = line_info[1]
					stock_list_dict["upper"] = line_info[2]
					stock_list_dict["lower"] = line_info[3]
				stock_list.append(stock_list_dict)
		self.__ui.update_stock_info(stock_list)
		stock_list = []
		with open("zs_pool.txt", "r") as f:
			for number, line in enumerate(f,start=1):
				line = line.strip('\n').strip('\r')
				if line != None:
					line = re.sub(' +', ' ', line)
					line_info = line.split(" ")
				name = line_info[0]
				stock_list_dict = {}
				stock_list_dict["stock_name"] = self.get_zs_name(name)
				stock_list_dict["up_down_percent"] = "unknow"
				stock_list_dict["value"] = "unknow"
				if len(line_info) == 2:
					stock_list_dict["notify"] = "1"
					stock_list_dict["limit"] = line_info[1]
				stock_list.append(stock_list_dict)
		self.__ui.update_zs_stock_info(stock_list)
	def start_get_info(self):
		stock_list = []
		with open("stock_pool.txt", "r") as f:
			stock_count = 0
			for number, line in enumerate(f,start=1):
				line = line.strip('\n')
				if line != None:
					line = re.sub(' +', ' ', line)
					line_info = line.split(" ")
				name = line_info[0]
				if name in self.stock_notify_already.keys():
					pass
				else:
					self.stock_notify_already[name] = 0
				stock_num=get_stock_num_by_name(name)
				if stock_num != None:
					return_value = get_gupiao_info(stock_num[1])
					if return_value != None:
						(prePrice, price, time) = return_value
						prePrice = float(prePrice)
						price = float(price)
						if price - prePrice > 0:
							up_down_percent_num = str((price -prePrice) / prePrice * 100 + 0.005)[0:4]
							up_down_percent = str((price -prePrice) / prePrice * 100 + 0.005)[0:4] + '%'
							up_down_value = str(price - prePrice + 0.005)[0:4]
						else:
							up_down_percent_num = up_down_percent = str((price -prePrice) / prePrice * 100 - 0.005)[0:5]
							up_down_percent = str((price -prePrice) / prePrice * 100 - 0.005)[0:5] + '%'
							up_down_value = str(price - prePrice - 0.005)[0:5]
						value = str(price)
						stock_list_dict = {}
						stock_list_dict["stock_name"] = name
						stock_list_dict["up_down_percent"] = up_down_percent
						stock_list_dict["up_down_value"] = up_down_value
						stock_list_dict["value"] = value
						stock_list.append(stock_list_dict)
						float_up_down = float(up_down_percent_num)
						notify = self.__ui.get_notify_value(stock_count)
						limit = self.__ui.get_limit_value(stock_count)
						upper_value = self.__ui.get_upper_value(stock_count)
						lower_value = self.__ui.get_lower_value(stock_count)
						try:
							notify = float(notify)
						except:
							#print("notifty exception here")
							continue
						if (notify == 1):
							try:
								limit = float(limit)
								if (abs(float_up_down) > abs(limit)) and (limit != 0):
									self.notify_user_message(stock_list_dict["stock_name"], float_up_down, limit, notify_method)
							except:
								#print("limit exception here")
								pass
							try:
								upper_value = float(upper_value)
								if (price > upper_value):
									self.notify_user_message(stock_list_dict["stock_name"], float_up_down, upper_value, notify_method)
							except:
								#print("uppper exception here")
								pass						
							try:
								lower_value = float(lower_value)
								if (price < lower_value):
									self.notify_user_message(stock_list_dict["stock_name"], float_up_down, lower_value, notify_method)
							except:
								#print("lower exception here")
								pass						
						stock_count = stock_count + 1
		self.__ui.update_stock_info(stock_list)
	def _update(self):
		try:
			self._set_count()
			self.update_notify_when_new_day()
			threading.Timer(1, self._update).start()
		except:
			print("something wrong happens, do the update again")
			os.system("sleep 3")
			self._update()
	def start(self):
		self.running_cnt = self.running_cnt + 1
		print("running the programme......running count:", self.running_cnt)
		self._update()
	def _set_count(self):
		if self.is_deal_time_now() == False:
			pass
		else:
			self.start_get_zs_info()
			self.start_get_info()
	def update_notify_when_new_day(self):
		time_now = time.localtime(time.time()).tm_mday
		if (self.pre_date_day == 0):
			self.pre_date_day = time_now
		else:
			if time_now != self.pre_date_day:
				self.update_stock_notify()
	def is_deal_time_now(self):
		if self.debug == True:
			return True
		time_now = time.localtime()
		if (time_now.tm_hour == 9) and (time_now.tm_min > 15):
			return True
		if (time_now.tm_hour == 10):
			return True
		if (time_now.tm_hour == 11) and (time_now.tm_min <= 30):
			return True
		if (time_now.tm_hour >= 13) and (time_now.tm_hour <= 15):
			return True
		return False
	def update_stock_notify(self):
		for kv in self.stock_notify_already:
			self.stock_notify_already[kv] = 1
if __name__=='__main__':
	app=QApplication(sys.argv)
	w=MyWidgets()
	w.show()
	sys.exit(app.exec_())

