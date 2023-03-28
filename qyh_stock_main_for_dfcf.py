#!/usr/bin/python3
# -*- coding: utf-8 -*-

#ui python files
from qyh_stock import Ui_MainWindow
from edit import EditWindow

#function python files
from search_stock_name import get_stock_num_by_name
from get_dfcfgupiao import get_gupiao_info
from basic_function import *

#system python files
import sys, time, threading
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os, re
import signal

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
        self.ui.restart_button.clicked.connect(self.close)

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
        t = threading.Thread(target=self.start_get_stock_info)
        #  t.start()
        thread_list.append(t)
        t = threading.Thread(target=self.get_compare_info)
        #  t.start()
        thread_list.append(t)
        for t in thread_list:
            t.start()
        for t in thread_list:
            t.join()

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

    def close(self):
        os.system('(sleep 2;./qyh_stock_main_for_dfcf.py)&')
        os.system('killall -9 qyh_stock_main_for_dfcf.py')
    def start_get_zs_info(self):
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
                    zs_stock_one_element_info = {}

                    #  zs_stock_one_element_info["stock_name"] = self.get_zs_name(name)
                    zs_stock_one_element_info["stock_name"] = line_info[0]
                    zs_stock_one_element_info["value"] = value
                    zs_stock_one_element_info["up_down_percent"] = up_down_percent_result
                    float_up_down = float(up_down_percent)
                    notify = self.ui.get_zs_notify_value(zs_stock_one_element_info["stock_name"])
                    zs_stock_one_element_info["notify"] = notify
                    #print("notify ", zs_stock_one_element_info["stock_name"], notify)
                    limit = str(self.ui.get_zs_limit_value(zs_stock_one_element_info["stock_name"]))
                    cnt = cnt + 1
                    if notify == True:
                        try:
                            limit = float(limit)
                            if (abs(float_up_down) > abs(limit)) and (notify == true) and (limit != 0):
                                zs_stock_one_element_info["color"] = "red"
                                notify_user_message(zs_stock_one_element_info["stock_name"], float_up_down, limit, notify_method)
                        except:
                            pass
                    zs_info_list.append(zs_stock_one_element_info)
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
                stock_one_element = {}
                stock_one_element["stock_name"] = name
                stock_one_element["up_down_percent"] = "unknow"
                stock_one_element["up_down_value"] = "unknow"
                stock_one_element["value"] = "unknow"
                stock_one_element["notify"] = False
                print(line_info)
                if len(line_info) == 5:
                    notify = line_info[1]
                    stock_one_element["limit"] = line_info[2]
                    stock_one_element["upper"] = line_info[3]
                    stock_one_element["lower"] = line_info[4]
                    if notify == "1":
                        stock_one_element["notify"] = True
                stock_list.append(stock_one_element)
        self.ui.update_stock_info(stock_list)
        zs_stock_list = []
        with open("zs_pool.txt", "r") as f:
            for number, line in enumerate(f,start=1):
                line = line.strip('\n').strip('\r')
                if line != None:
                    line = re.sub(' +', ' ', line)
                    line_info = line.split(" ")
                name = line_info[0]
                zs_stock_one_element = {}
                #  stock_list_dict["stock_name"] = self.get_stock_code_by_name(name)
                zs_stock_one_element["stock_name"] = line_info[0]
                zs_stock_one_element["up_down_percent"] = "unknow"
                zs_stock_one_element["value"] = "unknow"
                zs_stock_one_element["notify"] = False
                if len(line_info) == 3:
                    notify = line_info[1]
                    zs_stock_one_element["limit"] = line_info[2]
                    if notify == "1":
                        zs_stock_one_element["notify"] = True
                zs_stock_list.append(zs_stock_one_element)
        self.ui.update_zs_stock_info(zs_stock_list)
        compare_stock_list = []
        with open("compare_stock.txt", "r") as f:
            for number, line in enumerate(f,start=1):
                line = line.strip('\n').strip('\r')
                if line != None:
                    line = re.sub(' +', ' ', line)
                    line_info = line.split(" ")
                name_1 = line_info[0]
                name_2 = line_info[1]
                compare_stock_one_element = {}
                #  stock_list_dict["stock_name"] = self.get_stock_code_by_name(name)
                compare_stock_one_element["stock_name_1"] = line_info[0]
                compare_stock_one_element["up_down_percent_1"] = "unknow"
                compare_stock_one_element["stock_name_2"] = line_info[1]
                compare_stock_one_element["up_down_percent_2"] = "unknow"
                compare_stock_one_element["notify"] = False
                if len(line_info) == 4:
                    notify = line_info[2]
                    compare_stock_one_element["limit"] = line_info[3]
                    if notify == "1":
                        compare_stock_one_element["notify"] = True
                compare_stock_list.append(compare_stock_one_element)
        self.ui.update_compare_stock_info(compare_stock_list)

    def get_compare_info(self):
        stock_list = []
        float_up_down_1 = 0
        float_up_down_2 = 0
        with open("compare_stock.txt", "r") as f:
            stock_count = 0
            for number, line in enumerate(f,start=1):
                line = line.strip('\n')
                if line != None:
                    line = re.sub(' +', ' ', line)
                    line_info = line.split(" ")
                name_1 = line_info[0]
                name_2 = line_info[1]
                compare_one_element = {}
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
                        compare_one_element["stock_name_1"] = name_1
                        compare_one_element["up_down_percent_1"] = up_down_percent
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
                    compare_one_element["stock_name_2"] = name_2
                    compare_one_element["up_down_percent_2"] = up_down_percent
                    float_up_down_2 = float(up_down_percent_num)
                else:
                    continue
                notify = self.ui.get_compare_notify_value(name_1, name_2)
                limit = self.ui.get_compare_limit_value(name_1, name_2)
                if notify == True:
                    try:
                        limit = float(limit)
                        if (abs(float_up_down_2 - float_up_down_1) > abs(limit)) and (limit != 0):
                            compare_notify(name_1 + name_2, name_1 + compare_one_element["up_down_percent_1"] + name_2 + compare_one_element["up_down_percent_2"], "mail")
                            compare_one_element["color"] = "red"
                    except:
                        pass
                stock_list.append(compare_one_element)
        self.ui.update_compare_stock_info(stock_list)

    def start_get_stock_info(self):
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
                        stock_one_element = {}
                        stock_one_element["stock_name"] = name
                        stock_one_element["up_down_percent"] = up_down_percent
                        stock_one_element["up_down_value"] = up_down_value
                        stock_one_element["value"] = value
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
                                    notify_user_message(stock_one_element["stock_name"], float_up_down, limit, notify_method)
                                    stock_one_element["color"] = "red"
                            except:
                                #print("limit exception here")
                                pass
                            try:
                                upper_value = float(upper_value)
                                if (price > upper_value):
                                    notify_user_message(stock_one_element["stock_name"], float_up_down, upper_value, notify_method)
                                    stock_one_element["color"] = "red"
                            except:
                                #print("uppper exception here")
                                pass
                            try:
                                lower_value = float(lower_value)
                                if (price < lower_value):
                                    notify_user_message(stock_one_element["stock_name"], float_up_down, lower_value, notify_method)
                                    stock_one_element["color"] = "red"
                            except:
                                #print("lower exception here")
                                pass
                        stock_list.append(stock_one_element)
        self.ui.update_stock_info(stock_list)

    def start(self):
        self._update()
    def _update(self):
        try:
            self.main_do_things()
            threading.Timer(1, self._update).start()
        except:
            print("something wrong happens, do the update again")
            time.sleep(3)
            self._update()
    def main_do_things(self):
        self.running_cnt = self.running_cnt + 1
        update_notify_when_new_day()
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


def exit_handle(signum, frame):
    print('You choose to stop me.')
    os.system('killall -9 qyh_stock_main_for_dfcf.py')
if __name__=='__main__':
    app=QApplication(sys.argv)
    signal.signal(signal.SIGINT, exit_handle)
    signal.signal(signal.SIGTERM, exit_handle)
    w=MyWidgets()
    #edit_w = UiEditWindow()
    edit_w = MyEditWindow()
    #w.ui.pushButton_3.clicked.connect(edit_w.open)
    edit_w.ui.c.save_signal.connect(w.save_signal_slot)
    #w.ui.c.w_save_signal(w.save_signal_slot)
    w.show()
    sys.exit(app.exec_())

