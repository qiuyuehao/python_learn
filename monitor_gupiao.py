#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from search_stock_name import get_stock_num_by_name
from get_dfcfgupiao import get_gupiao_info
import sys, time, threading
import urllib.request
from PyQt5.QtWidgets import *
import os, re

def compare_gupiao_info_from_file():
	with open("monitor_pool.txt", "r") as f:
		for number, line in enumerate(f,start=1):
			line = line.strip('\n')
			if line != None:
				line_info = line.split(" ")
			name1 = line_info[0]
			name2 = line_info[1]
			limit = float(line_info[2])
			compare_the_infor(name1, name2, limit)
				
def compare_the_infor(stock_one, stock_two, limit):
	stock_num=get_stock_num_by_name(stock_one)
	print(stock_num)
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
			up_down_percent_value = float(up_down_percent_num)
	else:
		return

	stock_num=get_stock_num_by_name(stock_two)
	print(stock_num)
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
			up_down_percent_value_2 = float(up_down_percent_num)
	else:
		return
	print("compare infor:", up_down_percent_value_2, up_down_percent_value)
	if abs(up_down_percent_value_2 - up_down_percent_value) > limit:
		print("should notify the difference now")
if __name__=='__main__':
	compare_gupiao_info_from_file()