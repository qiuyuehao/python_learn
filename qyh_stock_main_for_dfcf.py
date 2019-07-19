#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from qyh_stock import Ui_MainWindow
from search_stock_name import get_stock_num_by_name
from get_dfcfgupiao import get_gupiao_info
import sys, time, threading
import urllib.request
from PyQt5.QtWidgets import *
from send_mail import send_mail_to_myself
import os

number_mail_send=[0,0,0,0,0]
zs_mail_send=[0,0,0,0,0]
zs_list=['000001', '399001', '399006']
class MyWidgets(QWidget):
	msec = 1000
	def __init__(self):
		super().__init__()
		self.__ui=Ui_MainWindow()
		self.__ui.setupUi(self)
		self.__ui.pushButton_2.clicked.connect(self.close)
		self.__ui.pushButton.clicked.connect(self.start)
		self.__ui.shangzhen.setText("上证指数")
		self.__ui.lineEdit_11.setText("1.5")
		self.__ui.shenzhen.setText("深证成指")
		self.__ui.lineEdit_12.setText("1.5")
		self.__ui.chuanyeban.setText("创业板")
		self.__ui.lineEdit_13.setText("2.0")
	def close(self):
		os.system('killall -9 qyh_stock_main_for_dfcf.py')
	def start_get_zs_info(self):
		#print(len(zs_list))
		cnt = 0
		for str_zs in zs_list:
			#print(str_zs)
			return_value = get_gupiao_info(str_zs)
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
				if cnt == 0:
					self.__ui.label_4.setText(value)
					self.__ui.label_5.setText(up_down_percent_result)
					#self.__ui.label.setText(value)
					limit = self.__ui.lineEdit_11.text()
					mail_title = "上证指数 "
				elif cnt == 1:
					self.__ui.label_6.setText(value)
					self.__ui.label_7.setText(up_down_percent_result)
					limit = self.__ui.lineEdit_12.text()
					mail_title = "深证成指 "
				elif cnt == 2:
					self.__ui.label_8.setText(value)
					self.__ui.label_9.setText(up_down_percent_result)
					limit = self.__ui.lineEdit_13.text()
					mail_title = "创业板 "

				cnt = cnt + 1
				float_up_down = float(up_down_percent)
				try:
					limit = float(limit)
				except:
					continue
				if abs(float_up_down) > abs(limit):
					#print("cnt is:", zs_mail_send[cnt - 1])
					if float_up_down > 0:
						if (zs_mail_send[cnt - 1] == 0):
							zs_mail_send[cnt - 1] = 1
							#print("cnt is:", zs_mail_send[cnt - 1])
							send_mail_to_myself(mail_title+"up up up", "congraduation")
						else:
							#print("cnt is:", zs_mail_send[cnt - 1])
							print(mail_title+"up up up...", "congraduation")
					else:
						if (zs_mail_send[cnt - 1] == 0):
							zs_mail_send[cnt - 1] = 1
							#print("cnt is:", zs_mail_send[cnt - 1])
							send_mail_to_myself(mail_title+"down down down", "please don't be upset, you don't mean it")
						else:
							#print("cnt is:", zs_mail_send[cnt - 1])
							print(mail_title+"down down down...", "please don't be upset, you don't mean it")
	def start_get_info(self):
		with open("stock_pool.txt", "r") as f:
			for number, line in enumerate(f,start=1):
				line = line.strip('\n')
				#print(line)
				stock_num=get_stock_num_by_name(line)
				if stock_num != None:
					#print("get stock_num:", stock_num[1])
					return_value = get_gupiao_info(stock_num[1])
					if return_value != None:
						(prePrice, price, time) = return_value
						prePrice = float(prePrice)
						price = float(price)
						if price - prePrice > 0:
							up_down_percent = str((price -prePrice) / prePrice * 100 + 0.005)[0:4] + '%'
							up_down_value = str(price - prePrice + 0.005)[0:4]
						else:
							up_down_percent = str((price -prePrice) / prePrice * 100 - 0.005)[0:5] + '%'
							up_down_value = str(price - prePrice - 0.005)[0:5]
						value = str(price)
						if number == 1:
							self.__ui.label_10.setText(line)
							self.__ui.label_12.setText(up_down_percent)
							self.__ui.label_11.setText(up_down_value)
							self.__ui.label.setText(value)
							should_notify = self.__ui.lineEdit.text()
							limit = self.__ui.lineEdit_2.text()
							try:
								limit = float(limit)
							except:
								continue
						if number == 2:
							self.__ui.label_13.setText(line)
							self.__ui.label_15.setText(up_down_percent)
							self.__ui.label_14.setText(up_down_value)
							self.__ui.label_2.setText(value)
							should_notify = self.__ui.lineEdit_3.text()
							limit = self.__ui.lineEdit_4.text()
							try:
								limit = float(limit)
							except:
								continue
						if number == 3:
							self.__ui.label_16.setText(line)
							self.__ui.label_18.setText(up_down_percent)
							self.__ui.label_17.setText(up_down_value)
							self.__ui.label_3.setText(value)
							should_notify = self.__ui.lineEdit_5.text()
							limit = self.__ui.lineEdit_6.text()
							try:
								limit = float(limit)
							except:
								continue
						if number == 4:
							self.__ui.label_19.setText(line)
							self.__ui.label_21.setText(up_down_percent)
							self.__ui.label_20.setText(up_down_value)
							self.__ui.label_25.setText(value)
							should_notify = self.__ui.lineEdit_7.text()
							limit = self.__ui.lineEdit_8.text()
							try:
								limit = float(limit)
							except:
								continue
						if number == 5:
							self.__ui.label_22.setText(line)
							self.__ui.label_24.setText(up_down_percent)
							self.__ui.label_23.setText(up_down_value)
							self.__ui.label_26.setText(value)
							should_notify = self.__ui.lineEdit_9.text()
							limit = self.__ui.lineEdit_10.text()
							try:
								limit = float(limit)
							except:
								continue

						if should_notify == "1":
							float_up_down = float(up_down_percent)
							if abs(float_up_down) > abs(limit):
								if float_up_down > 0:
									if (number_mail_send[number - 1] == 0):
										number_mail_send[number - 1] = 1
										send_mail_to_myself(line+"up up up", "congraduation")
									else:
										print(line+"up up up...", "congraduation")
								else:
									if (number_mail_send[number - 1] == 0):
										number_mail_send[number - 1] = 1										
										send_mail_to_myself(line+"down down down", "please don't be upset, you don't mean it")
									else:										
										print(line+"down down down...", "please don't be upset, you don't mean it")
	def get_stock_info(self,num_retries=2):
		#stock_no = self.__ui.lineEdit.text()
		stock_no = '000002'
		try: 
			url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd='+stock_no.strip()+'2&sty=CTBF&st=z&sr=&p=&ps=&cb=var%20pie_data=&js=(x)&token=28758b27a75f62dc3065b81f7facb365&_=1496312544427' 
			headers = {'User-agent':'WSWP'} 
			#request = urllib.Request(url,headers=headers) 
			page = urllib.request.urlopen(url) 
			#print(url)
			page_content = page.read() 
		except urllib.request.URLError as e: 
			print('download error:',e.reason) 
			page_content = None 
			if num_retries > 0:
				if hasattr(e,'code' and 500 <= e.code <600): # recursively retry 5xx HTTP errors 
					return get_stock_info(stock_no,num_retries-1) 
		return page_content
	def _update(self):
		try:
			self._set_count()
			#self.timer = self.after(self.msec,self._update)
			threading.Timer(1, self._update).start()
		except:
			print("something wrong happens, do the update again")
			os.system("sleep 3")
			self._update()
	def start(self):
		self._update()
	def _set_count(self):
		self.start_get_zs_info()
		self.start_get_info()
		#stock_info = self.get_stock_info()
		#if stock_info is not None:
			#stock_info = str(stock_info)
			#stock_info = stock_info.split(",")
			#print(stock_info)
			#stock_value = stock_info[4]
			#print(stock_value)
			#stock_info = stock_info[14:64]
		#self.__ui.label.setText(stock_value)
if __name__=='__main__':
	app=QApplication(sys.argv)
	w=MyWidgets()
	#w.move(400,200)
	w.show()
	sys.exit(app.exec_())
	