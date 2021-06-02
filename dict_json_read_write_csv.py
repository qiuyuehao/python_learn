#!/usr/bin/python3

# -*-coding:utf8-*-
# 需要的模块

f = open("stock_monitor.csv", "r")
read_line_index = 1
dict_key = ""

stock_list = list()
for line in f.readlines():
    line = line.strip('\n')  #去掉列表中每一个元素的换行符
    if (read_line_index == 1):
        dict_key = line
        dict_key = dict_key.split(",")
        print(dict_key)
    else:
        print(line)
        stock_info = line.split(",")
        i = 0
        stock_dict = dict()
        for key in dict_key:
            stock_dict[key] = stock_info[i]
            i = i + 1
        stock_list.append(stock_dict)
    read_line_index = read_line_index + 1

print(stock_list)
