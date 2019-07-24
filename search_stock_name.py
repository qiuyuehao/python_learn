#!/usr/bin/python3.5
import csv
#-*-coding:utf-8-*-

def get_stock_num_by_name(name):
	if name.isdigit():
		return [name,name]
	#print("get_stock_num_by_name :", name)
	with open('./stock/stock.csv', 'r') as f:
		rander = csv.reader(f)
		for i in rander:
			if i[0] == name:
				return i
		return None