#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from qyh_stock import Ui_MainWindow
from search_stock_name import get_stock_num_by_name
from get_baidugupiao import get_gupiao_info, get_szzs
import sys, time, threading
import urllib.request
from PyQt5.QtWidgets import *

class MyWidgets(QWidget):
	msec = 1000
	def __init__(self):
		super().__init__()
		self.__ui=Ui_MainWindow()
		self.__ui.setupUi(self)
		self.__ui.pushButton_2.clicked.connect(self.close)
		self.__ui.pushButton.clicked.connect(self.start)
	def start_get_info(self):
		with open("stock_pool.txt", "r") as f:
			for number, line in enumerate(f,start=1):
				line = line.strip('\n')
				print(line)
				stock_num=get_stock_num_by_name(line)
				if stock_num != None:
					print("get stock_num:", stock_num[1])
					return_value = get_gupiao_info(stock_num[1])
					if return_value != None:
						(value, up_down_percent, up_down_value) = return_value
						if number == 1:
							self.__ui.label_10.setText(line)
							self.__ui.label_12.setText(up_down_percent)
							self.__ui.label_11.setText(up_down_value)
							self.__ui.label.setText(value)
							if "1" == (self.__ui.lineEdit.text()):
								print("should notify")
								limit = self.__ui.lineEdit_2.text()
								#compare
							else:
								print("no need notify")
						if number == 2:
							self.__ui.label_13.setText(line)
							self.__ui.label_15.setText(up_down_percent)
							self.__ui.label_14.setText(up_down_value)
							self.__ui.label_2.setText(value)
						if number == 3:
							self.__ui.label_16.setText(line)
							self.__ui.label_18.setText(up_down_percent)
							self.__ui.label_17.setText(up_down_value)
							self.__ui.label_3.setText(value)
							print(self.__ui.lineEdit.text())
						if number == 4:
							self.__ui.label_19.setText(line)
							self.__ui.label_21.setText(up_down_percent)
							self.__ui.label_20.setText(up_down_value)
							self.__ui.label_25.setText(value)
						if number == 5:
							self.__ui.label_22.setText(line)
							self.__ui.label_24.setText(up_down_percent)
							self.__ui.label_23.setText(up_down_value)
							self.__ui.label_26.setText(value)
	def get_stock_info(self,num_retries=2):
		stock_no = self.__ui.lineEdit.text()
		try: 
			url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd='+stock_no.strip()+'2&sty=CTBF&st=z&sr=&p=&ps=&cb=var%20pie_data=&js=(x)&token=28758b27a75f62dc3065b81f7facb365&_=1496312544427' 
			headers = {'User-agent':'WSWP'} 
			#request = urllib.Request(url,headers=headers) 
			page = urllib.request.urlopen(url) 
			page_content = page.read() 
		except urllib.request.URLError as e: 
			print('download error:',e.reason) 
			page_content = None 
			if num_retries > 0:
				if hasattr(e,'code' and 500 <= e.code <600): # recursively retry 5xx HTTP errors 
					return get_stock_info(stock_no,num_retries-1) 
		return page_content
	def _update(self):
		self._set_count()
		#self.timer = self.after(self.msec,self._update)
		threading.Timer(1, self._update).start()
	def start(self):
		self._update()
	def _set_count(self):
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
	