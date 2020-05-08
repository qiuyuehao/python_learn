#!/usr/local/python3/bin/python3
# -*- coding: utf-8 -*-

from qyh_stock import Ui_MainWindow
from search_stock_name import get_stock_num_by_name
from get_dfcfgupiao import get_gupiao_info
import sys, time, threading
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from monitor_gupiao import compare_gupiao_info_from_file
import os, re
from edit import EditWindow
from edit import Communicate
from basic_function import *
from get_weibo import send_weibo_mail_on_time


notify_method = "mail"

class MyEditWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = EditWindow()
        self.ui.setupUi(self)
    def open(self):
        self.ui.open_file_all()
        self.show()
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        if e.key() == QtCore.Qt.Key_C:
            if e.modifiers() & QtCore.Qt.ControlModifier:
                print("ctrl + c press")
                self.close()
class MyWidgets(QWidget):
    msec = 1000
    pre_date_day = 0;
    running_cnt = 0
    stock_notify_already = {}
    debug = False
    update_running = 0
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.close)
        #  self.ui.pushButton.clicked.connect(self.start)
        #self.ui.pushButton_3.clicked.connect(self.edit)
        #  t = threading.Thread(target=self.get_and_update_init_stock_info)
        #  t.start()
        try:
           t = threading.Thread(target=send_weibo_mail_on_time)
           t.start()
        except:
            print("init send weibo mail fail")
        self.get_and_update_init_stock_info()
        try:
           t = threading.Thread(target=self.update_info_to_ui)
           t.start()
        except:
            print("init start fail")
        #  try:
           #  t = threading.Thread(target=self.update_info_to_ui)
           #  t.start()
        #  except:
            #  print("init 2 start fail")
        self.start()
    def closeEvent(self, event):
        event.accept()
        print("kill the programme")
        os.system('killall -9 qyh_stock_main_for_dfcf.py')
    def update_info_to_ui(self):
        thread_list = []
        t = threading.Thread(target=self.start_get_zs_info)
        #  t.start()
        thread_list.append(t)
        t = threading.Thread(target=self.start_get_info)
        #  t.start()
        thread_list.append(t)
        t = threading.Thread(target=self.get_compare_info)
        #  t.start()
        thread_list.append(t)
        for t in thread_list:
            t.start()
        for t in thread_list:
            t.join()
        #  self.start_get_zs_info()
        #  self.start_get_info()
        #  self.get_compare_info()
    def get_zs_name(self, zs_str):
        if zs_str == "000001":
            return str("上证指数")
        elif zs_str == "399001":
            return str("深证指数")
        elif zs_str == "399006":
            return str("创业板")
        else:
            return str("未知指数")
    def get_stock_code_by_name(self, name):
        if name == "上证指数":
            return str("000001")
        elif name == "深证指数":
            return str("399001")
        elif name == "创业板":
            return str("399006")
        else:
            return str("未知指数")
    def edit(self):
        print("not implement, please wait")
        #w.hide()
        #edit_w = UiEditWindow()
        #edit_w.setupUi(self)
        #edit_w.exec()
    def close(self):
        os.system('(sleep 1;./qyh_stock_main_for_dfcf.py)&')
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
                name = self.get_stock_code_by_name(name)
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

                    #  zs_stock_info["stock_name"] = self.get_zs_name(name)
                    zs_stock_info["stock_name"] = line_info[0]
                    zs_stock_info["value"] = value
                    zs_stock_info["up_down_percent"] = up_down_percent_result
                    float_up_down = float(up_down_percent)
                    notify = self.ui.get_zs_notify_value(zs_stock_info["stock_name"])
                    zs_stock_info["notify"] = notify
                    #print("notify ", zs_stock_info["stock_name"], notify)
                    limit = str(self.ui.get_zs_limit_value(zs_stock_info["stock_name"]))
                    cnt = cnt + 1
                    if notify == True:
                        try:
                            limit = float(limit)
                            if (abs(float_up_down) > abs(limit)) and (notify == true) and (limit != 0):
                                zs_stock_info["color"] = "red"
                                notify_user_message(zs_stock_info["stock_name"], float_up_down, limit, notify_method)
                        except:
                            pass
                    zs_info_list.append(zs_stock_info)
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
                stock_list_dict["notify"] = False
                if len(line_info) == 2:
                    stock_list_dict["limit"] = line_info[1]
                    try:
                        if float(stock_list_dict["limit"]) != 0:
                            stock_list_dict["notify"] = True
                    except:
                        pass
                if len(line_info) == 3:
                    stock_list_dict["notify"] = True
                    stock_list_dict["limit"] = line_info[1]
                    stock_list_dict["upper"] = line_info[2]
                if len(line_info) == 4:
                    stock_list_dict["notify"] = True
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
                #  stock_list_dict["stock_name"] = self.get_stock_code_by_name(name)
                stock_list_dict["stock_name"] = line_info[0]
                stock_list_dict["up_down_percent"] = "unknow"
                stock_list_dict["value"] = "unknow"
                stock_list_dict["notify"] = False
                if len(line_info) == 2:
                    stock_list_dict["notify"] = True
                    stock_list_dict["limit"] = line_info[1]
                stock_list.append(stock_list_dict)
        self.ui.update_zs_stock_info(stock_list)
        stock_list = []
        with open("monitor_pool.txt", "r") as f:
            for number, line in enumerate(f,start=1):
                line = line.strip('\n').strip('\r')
                if line != None:
                    line = re.sub(' +', ' ', line)
                    line_info = line.split(" ")
                name_1 = line_info[0]
                name_2 = line_info[1]
                stock_list_dict = {}
                #  stock_list_dict["stock_name"] = self.get_stock_code_by_name(name)
                stock_list_dict["stock_name_1"] = line_info[0]
                stock_list_dict["up_down_percent_1"] = "unknow"
                stock_list_dict["stock_name_2"] = line_info[1]
                stock_list_dict["up_down_percent_2"] = "unknow"
                stock_list_dict["notify"] = False
                if len(line_info) == 3:
                    stock_list_dict["notify"] = True
                    stock_list_dict["limit"] = line_info[2]
                stock_list.append(stock_list_dict)
        self.ui.update_compare_stock_info(stock_list)
    def get_compare_info(self):
        stock_list = []
        float_up_down_1 = 0
        float_up_down_2 = 0
        with open("monitor_pool.txt", "r") as f:
            stock_count = 0
            for number, line in enumerate(f,start=1):
                line = line.strip('\n')
                if line != None:
                    line = re.sub(' +', ' ', line)
                    line_info = line.split(" ")
                name_1 = line_info[0]
                name_2 = line_info[1]
                stock_list_dict = {}
                stock_num=get_stock_num_by_name(name_1)
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
                        stock_list_dict["stock_name_1"] = name_1
                        stock_list_dict["up_down_percent_1"] = up_down_percent
                        float_up_down_1 = float(up_down_percent_num)
                    else:
                        continue
                else:
                    continue
                stock_num=get_stock_num_by_name(name_2)
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
                    stock_list_dict["stock_name_2"] = name_2
                    stock_list_dict["up_down_percent_2"] = up_down_percent
                    float_up_down_2 = float(up_down_percent_num)
                else:
                    continue
                notify = self.ui.get_compare_notify_value(name_1, name_2)
                limit = self.ui.get_compare_limit_value(name_1, name_2)
                if notify == True:
                    try:
                        limit = float(limit)
                        if (abs(float_up_down_2 - float_up_down_1) > abs(limit)) and (limit != 0):
                            #  notify_user_message(stock_list_dict["stock_name"], float_up_down, limit, notify_method)
                            compare_notify(name_1 + name_2, name_1 + stock_list_dict["up_down_percent_1"] + name_2 + stock_list_dict["up_down_percent_2"], "mail")
                            stock_list_dict["color"] = "red"
                    except:
                        pass
                stock_list.append(stock_list_dict)
        self.ui.update_compare_stock_info(stock_list)
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
                if name.isdigit():
                    stock_num = (name, name)
                else:
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
                        float_up_down = float(up_down_percent_num)
                        notify = self.ui.get_notify_value_by_name(name)
                        limit = self.ui.get_limit_value_by_name(name)
                        upper_value = self.ui.get_upper_value_by_name(name)
                        lower_value = self.ui.get_lower_value_by_name(name)
                        stock_count = stock_count + 1
                        if (notify == True):
                            try:
                                limit = float(limit)
                                if (abs(float_up_down) > abs(limit)) and (limit != 0):
                                    notify_user_message(stock_list_dict["stock_name"], float_up_down, limit, notify_method)
                                    stock_list_dict["color"] = "red"
                            except:
                                #print("limit exception here")
                                pass
                            try:
                                upper_value = float(upper_value)
                                if (price > upper_value):
                                    notify_user_message(stock_list_dict["stock_name"], float_up_down, upper_value, notify_method)
                                    stock_list_dict["color"] = "red"
                            except:
                                #print("uppper exception here")
                                pass
                            try:
                                lower_value = float(lower_value)
                                if (price < lower_value):
                                    notify_user_message(stock_list_dict["stock_name"], float_up_down, lower_value, notify_method)
                                    stock_list_dict["color"] = "red"
                            except:
                                #print("lower exception here")
                                pass
                        stock_list.append(stock_list_dict)
        self.ui.update_stock_info(stock_list)
    def _update(self):
        try:
            self.main_do_things()
            threading.Timer(1, self._update).start()
        except:
            print("something wrong happens, do the update again")
            time.sleep(3)
            self._update()
    def start(self):
        threading.Timer(1, self._update).start()
    def main_do_things(self):
        self.running_cnt = self.running_cnt + 1
        update_notify_when_new_day()
        #  print("running the programme......running count:", self.running_cnt)
        if is_deal_time_now() == False:
            pass
        else:
            self.update_info_to_ui()

    def save_signal_slot(self, some_message):
        print("save signal", some_message)
        self.get_and_update_init_stock_info()
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        if e.key() == QtCore.Qt.Key_C:
            if e.modifiers() & QtCore.Qt.ControlModifier:
                print("ctrl + c press")
                self.close()
if __name__=='__main__':
    app=QApplication(sys.argv)
    w=MyWidgets()
    #edit_w = UiEditWindow()
    edit_w = MyEditWindow()
    w.ui.pushButton_3.clicked.connect(edit_w.open)
    edit_w.ui.c.save_signal.connect(w.save_signal_slot)
    #w.ui.c.w_save_signal(w.save_signal_slot)
    w.show()
    sys.exit(app.exec_())

