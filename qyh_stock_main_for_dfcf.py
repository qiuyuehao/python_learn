#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from qyh_stock import Ui_MainWindow
from search_stock_name import get_stock_num_by_name
from get_dfcfgupiao import get_gupiao_info
import sys, time, threading
import urllib.request
from PyQt5.QtWidgets import *
from monitor_gupiao import compare_gupiao_info_from_file
import os, re
from edit import EditWindow
from edit import Communicate
from basic_function import *


notify_method = "mail"

class MyEditWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = EditWindow()
        self.ui.setupUi(self)
    def open(self):
        self.show()

class MyWidgets(QWidget):
    msec = 1000
    pre_date_day = 0;
    running_cnt = 0
    stock_notify_already = {}
    debug = False
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.start)
        #self.ui.pushButton_3.clicked.connect(self.edit)
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
    def edit(self):
        print("not implement, please wait")
        #w.hide()
        #edit_w = UiEditWindow()
        #edit_w.setupUi(self)
        #edit_w.exec()
    def close(self):
        os.system('killall -9 qyh_stock_main_for_dfcf.py')
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
                    float_up_down = float(up_down_percent)
                    notify = str(self.ui.get_zs_notify_value(zs_stock_info["stock_name"]))
                    limit = str(self.ui.get_zs_limit_value(zs_stock_info["stock_name"]))
                    cnt = cnt + 1
                    try:
                        notify = float(notify)
                        limit = float(limit)
                    except:
                        continue
                    if (abs(float_up_down) > abs(limit)) and (notify == 1) and (limit != 0):
                        notify_user_message(zs_stock_info["stock_name"], float_up_down, limit, notify_method)
        self.ui.update_zs_stock_info(zs_info_list)
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
        self.ui.update_stock_info(stock_list)
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
        self.ui.update_zs_stock_info(stock_list)
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
                        notify = self.ui.get_notify_value_by_name(name)
                        limit = self.ui.get_limit_value_by_name(name)
                        upper_value = self.ui.get_upper_value_by_name(name)
                        lower_value = self.ui.get_lower_value_by_name(name)
                        stock_count = stock_count + 1
                        try:
                            notify = float(notify)
                        except:
                            #print("notifty exception here")
                            continue
                        if (notify == 1):
                            try:
                                limit = float(limit)
                                if (abs(float_up_down) > abs(limit)) and (limit != 0):
                                    notify_user_message(stock_list_dict["stock_name"], float_up_down, limit, notify_method)
                            except:
                                #print("limit exception here")
                                pass
                            try:
                                upper_value = float(upper_value)
                                if (price > upper_value):
                                    notify_user_message(stock_list_dict["stock_name"], float_up_down, upper_value, notify_method)
                            except:
                                #print("uppper exception here")
                                pass
                            try:
                                lower_value = float(lower_value)
                                if (price < lower_value):
                                    notify_user_message(stock_list_dict["stock_name"], float_up_down, lower_value, notify_method)
                            except:
                                #print("lower exception here")
                                pass
        self.ui.update_stock_info(stock_list)
    def _update(self):
        try:
            self._set_count()
            update_notify_when_new_day()
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
        if is_deal_time_now() == False:
            pass
        else:
            self.start_get_zs_info()
            self.start_get_info()

    def save_signal_slot(self, some_message):
        print("call signal slot here")
        self.get_and_update_init_stock_info()
        print(some_message)

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=MyWidgets()
    #edit_w = UiEditWindow()
    edit_w = MyEditWindow()
    w.ui.pushButton_3.clicked.connect(edit_w.open)
    edit_w.ui.c.save_signal.connect(w.save_signal_slot)
    w.show()
    sys.exit(app.exec_())

