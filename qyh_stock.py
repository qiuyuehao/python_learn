# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qyh_stock.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

init_valid_cnt = 3
class Ui_MainWindow(object):
    display_per_page = 7
    zs_display_per_page = 5
    compare_per_page = 5
    ui_list = []
    valid_stock_cnt = 0
    zs_list = []
    valid_zs_cnt = 0
    compare_list = []
    valid_compare_cnt = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("qyh_stock_win")
        MainWindow.resize(778, 851)
        MainWindow.setWindowIcon(QIcon('sea.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 200, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 260, 80, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 310, 80, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 370, 80, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.save_config_to_txt)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 671, 121))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        for i in range(0, self.zs_display_per_page):
            ui_list_dict = {}
            ui_list_dict["stock_name"] = QtWidgets.QLabel(self.widget)
            ui_list_dict["value"] = QtWidgets.QLabel(self.widget)
            ui_list_dict["up_down_percent"] = QtWidgets.QLabel(self.widget)
            ui_list_dict["notify"] = QtWidgets.QLineEdit(self.widget)
            ui_list_dict["limit"] = QtWidgets.QLineEdit(self.widget)
            ui_list_dict["valid_cnt"] = 0
            self.gridLayout.addWidget(ui_list_dict["stock_name"], 0, i, 1, 1)
            self.gridLayout.addWidget(ui_list_dict["up_down_percent"], 1, i, 1, 1)
            self.gridLayout.addWidget(ui_list_dict["value"], 2, i, 1, 1)
            self.gridLayout.addWidget(ui_list_dict["notify"], 3, i, 1, 1)
            self.gridLayout.addWidget(ui_list_dict["limit"], 4, i, 1, 1)
            self.zs_list.append(ui_list_dict)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 150, 572, 351))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setSpacing(10)
        for i in range(0, self.display_per_page):
            ui_list_dict = {}
            ui_list_dict["stock_name"] = QtWidgets.QLabel(self.widget1)
            ui_list_dict["up_down_value"] = QtWidgets.QLabel(self.widget1)
            ui_list_dict["up_down_percent"] = QtWidgets.QLabel(self.widget1)
            ui_list_dict["value"] = QtWidgets.QLabel(self.widget1)
            ui_list_dict["notify"] = QtWidgets.QLineEdit(self.widget1)
            ui_list_dict["limit"] = QtWidgets.QLineEdit(self.widget1)
            ui_list_dict["upper"] = QtWidgets.QLineEdit(self.widget)
            ui_list_dict["lower"] = QtWidgets.QLineEdit(self.widget)
            ui_list_dict["valid_cnt"] = 0
            self.gridLayout_3.addWidget(ui_list_dict["stock_name"], i, 0, 1, 1)
            self.gridLayout_3.addWidget(ui_list_dict["up_down_value"], i, 1, 1, 1)
            self.gridLayout_3.addWidget(ui_list_dict["up_down_percent"], i, 2, 1, 1)
            self.gridLayout_3.addWidget(ui_list_dict["value"], i, 3, 1, 1)
            self.gridLayout_3.addWidget(ui_list_dict["notify"], i, 4, 1, 1)
            self.gridLayout_3.addWidget(ui_list_dict["limit"], i, 5, 1, 1)
            self.gridLayout_3.addWidget(ui_list_dict["upper"], i, 6, 1, 1)
            self.gridLayout_3.addWidget(ui_list_dict["lower"], i, 7, 1, 1)
            self.ui_list.append(ui_list_dict)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(50, 430, 592, 351))
        self.widget2.setObjectName("widget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setSpacing(10)
        for i in range(0, self.compare_per_page):
            ui_list_dict = {}
            ui_list_dict["stock_name_1"] = QtWidgets.QLabel(self.widget1)
            ui_list_dict["up_down_percent_1"] = QtWidgets.QLabel(self.widget1)
            ui_list_dict["stock_name_2"] = QtWidgets.QLabel(self.widget1)
            ui_list_dict["up_down_percent_2"] = QtWidgets.QLabel(self.widget1)
            ui_list_dict["notify"] = QtWidgets.QLineEdit(self.widget1)
            ui_list_dict["limit"] = QtWidgets.QLineEdit(self.widget1)
            ui_list_dict["valid_cnt"] = 0
            self.gridLayout_4.addWidget(ui_list_dict["stock_name_1"], i, 0, 1, 1)
            self.gridLayout_4.addWidget(ui_list_dict["up_down_percent_1"], i, 1, 1, 1)
            self.gridLayout_4.addWidget(ui_list_dict["stock_name_2"], i, 2, 1, 1)
            self.gridLayout_4.addWidget(ui_list_dict["up_down_percent_2"], i, 3, 1, 1)
            self.gridLayout_4.addWidget(ui_list_dict["notify"], i, 4, 1, 1)
            self.gridLayout_4.addWidget(ui_list_dict["limit"], i, 5, 1, 1)
            self.compare_list.append(ui_list_dict)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def get_compare_notify_value(self, name1, name2):
        if len(self.compare_list) != 0:
            for i in range(0, len(self.compare_list)):
                if (name1 == self.compare_list[i]["stock_name_1"].text()) and (name2 == self.compare_list[i]["stock_name_2"].text()):
                    return self.compare_list[i]["notify"].text()
        return None
    def get_compare_limit_value(self, name1, name2):
        if len(self.compare_list) != 0:
            for i in range(0, len(self.compare_list)):
                if (name1 == self.compare_list[i]["stock_name_1"].text()) and (name2 == self.compare_list[i]["stock_name_2"].text()):
                    return self.compare_list[i]["limit"].text()
        return None
    def get_zs_notify_value(self, name):
        if len(self.zs_list) != 0:
            for i in range(0, len(self.zs_list)):
                if name == self.zs_list[i]["stock_name"].text():
                    return self.zs_list[i]["notify"].text()
        return None
    def get_zs_limit_value(self, name):
        if len(self.zs_list) != 0:
            for i in range(0, len(self.zs_list)):
                if name == self.zs_list[i]["stock_name"].text():
                    return self.zs_list[i]["limit"].text()
        return None
    def get_upper_value_by_name(self, name):
        if len(self.ui_list) != 0:
            for i in range(0, len(self.ui_list)):
                if name == self.ui_list[i]["stock_name"].text():
                    return self.ui_list[i]["upper"].text()
        return None
    def get_lower_value_by_name(self, name):
        if len(self.ui_list) != 0:
            for i in range(0, len(self.ui_list)):
                if name == self.ui_list[i]["stock_name"].text():
                    return self.ui_list[i]["lower"].text()
        return None
    def get_notify_value_by_name(self, name):
        if len(self.ui_list) != 0:
            for i in range(0, len(self.ui_list)):
                if name == self.ui_list[i]["stock_name"].text():
                    return self.ui_list[i]["notify"].text()
        return None
    def get_limit_value_by_name(self, name):
        if len(self.ui_list) != 0:
            for i in range(0, len(self.ui_list)):
                if name == self.ui_list[i]["stock_name"].text():
                    return self.ui_list[i]["limit"].text()
        return None
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "start"))
        self.pushButton_2.setText(_translate("MainWindow", "stop"))
        self.pushButton_3.setText(_translate("MainWindow", "edit"))
        self.pushButton_4.setText(_translate("MainWindow", "saveConfig"))
        MainWindow.setWindowTitle(_translate("MainWindow", "qyh_stock_win"))
    def update_compare_stock_info(self, stock_info):
        stock_len = len(stock_info)
        len_ui_list = len(self.compare_list)
        for i in range(0, stock_len):
            found = 0
            for j in range(0, len_ui_list):
                if (self.compare_list[j]["stock_name_1"].text() == stock_info[i]["stock_name_1"]) and (self.compare_list[j]["stock_name_2"].text() == stock_info[i]["stock_name_2"]):
                    self.compare_list[j]["up_down_percent_1"].setText(stock_info[i]["up_down_percent_1"])
                    self.compare_list[j]["up_down_percent_2"].setText(stock_info[i]["up_down_percent_2"])
                    if "notify" in stock_info[i].keys():
                        self.compare_list[j]["notify"].setText(stock_info[i]["notify"])
                    if "limit" in stock_info[i].keys():
                        self.compare_list[j]["limit"].setText(stock_info[i]["limit"])
                    if "color" in stock_info[i].keys():
                        self.compare_list[j]["stock_name_1"].setStyleSheet('color:red;background-color:blue')
                    else:
                        self.compare_list[j]["stock_name_1"].setStyleSheet('')
                    found = 1
                    self.compare_list[j]["valid_cnt"] = init_valid_cnt
                    break
            if found == 0:#can not find a name match the stock_info, add a new one
                self.compare_list[self.valid_compare_cnt]["stock_name_1"].setText(stock_info[i]["stock_name_1"])
                self.compare_list[self.valid_compare_cnt]["up_down_percent_1"].setText(stock_info[i]["up_down_percent_1"])
                self.compare_list[self.valid_compare_cnt]["stock_name_2"].setText(stock_info[i]["stock_name_2"])
                self.compare_list[self.valid_compare_cnt]["up_down_percent_2"].setText(stock_info[i]["up_down_percent_2"])
                if "notify" in stock_info[i].keys():
                        self.compare_list[self.valid_compare_cnt]["notify"].setText(stock_info[i]["notify"])
                if "limit" in stock_info[i].keys():
                    self.compare_list[self.valid_compare_cnt]["limit"].setText(stock_info[i]["limit"])
                self.compare_list[self.valid_compare_cnt]["valid_cnt"] = init_valid_cnt
                self.valid_compare_cnt = self.valid_compare_cnt + 1
        for i in range(0, len_ui_list):
            if self.compare_list[i]["valid_cnt"] > 0:
                self.compare_list[i]["valid_cnt"] = self.compare_list[i]["valid_cnt"] - 1
            if self.compare_list[i]["valid_cnt"] > 0:
                can_see = True
            else:
                can_see = False
            self.compare_list[i]["stock_name_1"].setVisible(can_see)
            self.compare_list[i]["up_down_percent_1"].setVisible(can_see)
            self.compare_list[i]["stock_name_2"].setVisible(can_see)
            self.compare_list[i]["up_down_percent_2"].setVisible(can_see)
            self.compare_list[i]["limit"].setVisible(can_see)
            self.compare_list[i]["notify"].setVisible(can_see)
    def update_zs_stock_info(self, stock_info):
        stock_len = len(stock_info)
        len_ui_list = len(self.zs_list)
        for i in range(0, stock_len):
            found = 0
            for j in range(0, len_ui_list):
                if (self.zs_list[j]["stock_name"].text() == stock_info[i]["stock_name"]):
                    self.zs_list[j]["value"].setText(stock_info[i]["value"])
                    self.zs_list[j]["stock_name"].setText(stock_info[i]["stock_name"])
                    #self.zs_list[i]["up_down_value"].setText(stock_info[i]["up_down_value"])
                    self.zs_list[j]["up_down_percent"].setText(stock_info[i]["up_down_percent"])
                    if "notify" in stock_info[i].keys():
                        self.zs_list[j]["notify"].setText(stock_info[i]["notify"])
                    if "limit" in stock_info[i].keys():
                        self.zs_list[j]["limit"].setText(stock_info[i]["limit"])
                    if "color" in stock_info[i].keys():
                        self.zs_list[j]["stock_name"].setStyleSheet('color:red;background-color:blue')
                    else:
                        self.zs_list[j]["stock_name"].setStyleSheet('')
                    found = 1
                    self.zs_list[j]["valid_cnt"] = init_valid_cnt
                    break
            if found == 0:#can not find a name match the stock_info, add a new one
                self.zs_list[self.valid_zs_cnt]["stock_name"].setText(stock_info[i]["stock_name"])
                self.zs_list[self.valid_zs_cnt]["up_down_percent"].setText(stock_info[i]["up_down_percent"])
                self.zs_list[self.valid_zs_cnt]["value"].setText(stock_info[i]["value"])
                if "notify" in stock_info[i].keys():
                        self.zs_list[self.valid_zs_cnt]["notify"].setText(stock_info[i]["notify"])
                if "limit" in stock_info[i].keys():
                    self.zs_list[self.valid_zs_cnt]["limit"].setText(stock_info[i]["limit"])
                self.zs_list[self.valid_zs_cnt]["valid_cnt"] = init_valid_cnt
                self.valid_zs_cnt = self.valid_zs_cnt + 1
        for i in range(0, len_ui_list):
            if self.zs_list[i]["valid_cnt"] > 0:
                self.zs_list[i]["valid_cnt"] = self.zs_list[i]["valid_cnt"] - 1
            if self.zs_list[i]["valid_cnt"] > 0:
                can_see = True
            else:
                can_see = False
            self.zs_list[i]["value"].setVisible(can_see)
            self.zs_list[i]["stock_name"].setVisible(can_see)
            self.zs_list[i]["up_down_percent"].setVisible(can_see)
            self.zs_list[i]["notify"].setVisible(can_see)
            self.zs_list[i]["limit"].setVisible(can_see)
    def update_stock_info(self, stock_info):
        stock_len = len(stock_info)
        len_ui_list = len(self.ui_list)
        for i in range(0, stock_len):
            found = 0
            for j in range(0, len_ui_list):
                if (self.ui_list[j]["stock_name"].text() == stock_info[i]["stock_name"]):
                    self.ui_list[j]["value"].setText(stock_info[i]["value"])
                    self.ui_list[j]["stock_name"].setText(stock_info[i]["stock_name"])
                    self.ui_list[i]["up_down_value"].setText(stock_info[i]["up_down_value"])
                    self.ui_list[j]["up_down_percent"].setText(stock_info[i]["up_down_percent"])
                    if "notify" in stock_info[i].keys():
                        self.ui_list[j]["notify"].setText(stock_info[i]["notify"])
                    if "limit" in stock_info[i].keys():
                        self.ui_list[j]["limit"].setText(stock_info[i]["limit"])
                    if "upper" in stock_info[i].keys():
                        self.ui_list[j]["upper"].setText(stock_info[i]["upper"])
                    if "lower" in stock_info[i].keys():
                        self.ui_list[j]["lower"].setText(stock_info[i]["lower"])
                    if "color" in stock_info[i].keys():
                        self.ui_list[j]["stock_name"].setStyleSheet('color:red;background-color:blue')
                    else:
                        self.ui_list[j]["stock_name"].setStyleSheet('')
                    found = 1
                    self.ui_list[j]["valid_cnt"] = init_valid_cnt
                    break
            if found == 0:#can not find a name match the stock_info, add a new one
                self.ui_list[self.valid_stock_cnt]["stock_name"].setText(stock_info[i]["stock_name"])
                self.ui_list[self.valid_stock_cnt]["up_down_percent"].setText(stock_info[i]["up_down_percent"])
                self.ui_list[self.valid_stock_cnt]["value"].setText(stock_info[i]["value"])
                self.ui_list[self.valid_stock_cnt]["up_down_value"].setText(stock_info[i]["up_down_value"])
                self.ui_list[self.valid_stock_cnt]["value"].setText(stock_info[i]["value"])
                self.ui_list[self.valid_stock_cnt]["valid_cnt"] = init_valid_cnt
                if "notify" in stock_info[i].keys():
                        self.ui_list[self.valid_stock_cnt]["notify"].setText(stock_info[i]["notify"])
                if "limit" in stock_info[i].keys():
                    self.ui_list[self.valid_stock_cnt]["limit"].setText(stock_info[i]["limit"])
                if "upper" in stock_info[i].keys():
                        self.ui_list[self.valid_stock_cnt]["upper"].setText(stock_info[i]["upper"])
                if "lower" in stock_info[i].keys():
                    self.ui_list[self.valid_stock_cnt]["lower"].setText(stock_info[i]["lower"])
                self.valid_stock_cnt = self.valid_stock_cnt + 1
        for i in range(0, len_ui_list):
            if self.ui_list[i]["valid_cnt"] > 0:
                self.ui_list[i]["valid_cnt"] = self.ui_list[i]["valid_cnt"] - 1
            if self.ui_list[i]["valid_cnt"] > 0:
                can_see = True
            else:
                can_see = False
            self.ui_list[i]["value"].setVisible(can_see)
            self.ui_list[i]["stock_name"].setVisible(can_see)
            self.ui_list[i]["up_down_value"].setVisible(can_see)
            self.ui_list[i]["up_down_percent"].setVisible(can_see)
            self.ui_list[i]["notify"].setVisible(can_see)
            self.ui_list[i]["limit"].setVisible(can_see)
            self.ui_list[i]["upper"].setVisible(can_see)
            self.ui_list[i]["lower"].setVisible(can_see)
    def save_config_to_txt(self):
        len_ui_list = len(self.ui_list)
        save_stock_txt_str = None
        for i in range(0, self.valid_stock_cnt):
            if save_stock_txt_str == None:
                save_stock_txt_str = self.ui_list[i]["stock_name"].text()
            else:
                save_stock_txt_str = save_stock_txt_str + self.ui_list[i]["stock_name"].text()
            if self.ui_list[i]["limit"].text():
                save_stock_txt_str = save_stock_txt_str + " " + self.ui_list[i]["limit"].text()
                if self.ui_list[i]["upper"].text():
                    save_stock_txt_str = save_stock_txt_str + " " + self.ui_list[i]["upper"].text()
                if self.ui_list[i]["lower"].text():
                    save_stock_txt_str = save_stock_txt_str + " " + self.ui_list[i]["lower"].text()
            if i != self.valid_stock_cnt - 1:
                save_stock_txt_str = save_stock_txt_str + "\n"
        f = open("stock_pool.txt", "w")
        f.write(save_stock_txt_str)
        f.close()
        len_ui_list = len(self.zs_list)
        save_stock_txt_str = None

        for i in range(0, self.valid_zs_cnt):
            if save_stock_txt_str == None:
                save_stock_txt_str = self.zs_list[i]["stock_name"].text()
            else:
                save_stock_txt_str = save_stock_txt_str + self.zs_list[i]["stock_name"].text()
            if self.zs_list[i]["limit"].text():
                save_stock_txt_str = save_stock_txt_str + " " + self.zs_list[i]["limit"].text()
            if i != self.valid_zs_cnt - 1:
                save_stock_txt_str = save_stock_txt_str + "\n"
        f = open("zs_pool.txt", "w")
        f.write(save_stock_txt_str)
        f.close()
        len_ui_list = len(self.compare_list)
        save_stock_txt_str = None

        for i in range(0, self.valid_compare_cnt):
            if save_stock_txt_str == None:
                save_stock_txt_str = self.compare_list[i]["stock_name_1"].text() + ' ' + self.compare_list[i]["stock_name_2"].text()
            else:
                save_stock_txt_str = save_stock_txt_str + self.compare_list[i]["stock_name_1"].text() + ' ' + self.compare_list[i]["stock_name_2"].text()
            if self.compare_list[i]["limit"].text():
                save_stock_txt_str = save_stock_txt_str + " " + self.compare_list[i]["limit"].text()
            if i != self.valid_compare_cnt - 1:
                save_stock_txt_str = save_stock_txt_str + "\n"
        f = open("monitor_pool.txt", "w")
        f.write(save_stock_txt_str)
        f.close()

