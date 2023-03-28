# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qyh_stock.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

#class Communicate(QObject):
    #w_save_signal = pyqtSignal(str)

class Ui_MainWindow(object):
    valid_cnt = 3
    stock_display_per_page = 7
    zs_display_per_page = 5
    compare_per_page = 7
    stock_list = []
    valid_stock_cnt = 0
    zs_list = []
    valid_zs_cnt = 0
    compare_list = []
    valid_compare_cnt = 0
    c = None
    def setupUi(self, MainWindow):
        self.c = MainWindow
        MainWindow.setObjectName("stock_windows_designed_by_qyh")
        MainWindow.resize(778, 851)
        MainWindow.setWindowIcon(QIcon('sea.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.restart_button = QtWidgets.QPushButton(self.centralwidget)
        self.restart_button.setGeometry(QtCore.QRect(660, 260, 80, 25))
        self.restart_button.setObjectName("restart")

        self.save_config_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_config_button.setGeometry(QtCore.QRect(660, 370, 80, 25))
        self.save_config_button.setObjectName("save config")
        self.save_config_button.clicked.connect(self.save_config_to_txt)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 671, 121))
        self.widget.setObjectName("widget")

        self.zs_gridLayout = QtWidgets.QGridLayout(self.widget)
        self.zs_gridLayout.setContentsMargins(3, 3, 3, 3)
        self.zs_gridLayout.setSpacing(5)
        self.zs_gridLayout.setObjectName("zs_gridLayout")


        for i in range(0, self.zs_display_per_page):
            zs_ui_list_dict = {}
            zs_ui_list_dict["stock_name"] = QtWidgets.QLabel(self.widget)
            zs_ui_list_dict["value"] = QtWidgets.QLabel(self.widget)
            zs_ui_list_dict["up_down_percent"] = QtWidgets.QLabel(self.widget)
            zs_ui_list_dict["notify"] = QtWidgets.QCheckBox("notify", self.widget)
            zs_ui_list_dict["notify"].setTristate(False)
            zs_ui_list_dict["notify"].setChecked(False)
            zs_ui_list_dict["limit"] = QtWidgets.QLineEdit(self.widget)
            zs_ui_list_dict["valid_cnt"] = 0
            self.zs_gridLayout.addWidget(zs_ui_list_dict["stock_name"], 0, i, 1, 1)
            self.zs_gridLayout.addWidget(zs_ui_list_dict["up_down_percent"], 1, i, 1, 1)
            self.zs_gridLayout.addWidget(zs_ui_list_dict["value"], 2, i, 1, 1)
            self.zs_gridLayout.addWidget(zs_ui_list_dict["notify"], 3, i, 1, 1)
            self.zs_gridLayout.addWidget(zs_ui_list_dict["limit"], 4, i, 1, 1)
            self.zs_list.append(zs_ui_list_dict)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 572, 351))
        self.widget.setObjectName("widget")
        self.text_grid_layout = QtWidgets.QGridLayout(self.widget)
        #self.stock_grid_layout.setContentsMargins(10, 10, 10, 10)
        self.text_grid_layout.setObjectName("stock_grid_layout")
        self.text_grid_layout.setSpacing(10)

        ui_stock_name = QtWidgets.QLabel(self.widget)
        ui_up_down_value = QtWidgets.QLabel(self.widget)
        ui_up_down_percent = QtWidgets.QLabel(self.widget)
        ui_value = QtWidgets.QLabel(self.widget)
        ui_up_notify = QtWidgets.QLabel(self.widget)
        ui_up_limit = QtWidgets.QLabel(self.widget)
        ui_up_value_limit = QtWidgets.QLabel(self.widget)
        ui_down_value_limit = QtWidgets.QLabel(self.widget)
        ui_stock_name.setText("名称")
        ui_up_down_value.setText("涨跌")
        ui_up_down_percent.setText("涨跌幅")
        ui_value.setText("价格")
        ui_up_notify.setText("是否通知")
        ui_up_limit.setText("幅度百分比")
        ui_up_value_limit.setText("价格上限")
        ui_down_value_limit.setText("价格下限")
        self.text_grid_layout.addWidget(ui_stock_name, 0, 0, 1, 1)
        self.text_grid_layout.addWidget(ui_up_down_value, 0, 1, 1, 1)
        self.text_grid_layout.addWidget(ui_up_down_percent, 0, 2, 1, 1)
        self.text_grid_layout.addWidget(ui_value, 0, 3, 1, 1)
        self.text_grid_layout.addWidget(ui_up_notify, 0, 4, 1, 1)
        self.text_grid_layout.addWidget(ui_up_limit, 0, 5, 1, 1)
        self.text_grid_layout.addWidget(ui_up_value_limit, 0, 6, 1, 1)
        self.text_grid_layout.addWidget(ui_down_value_limit, 0, 7, 1, 1)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 170, 572, 351))
        self.widget.setObjectName("widget")
        self.stock_grid_layout = QtWidgets.QGridLayout(self.widget)
        self.stock_grid_layout.setObjectName("stock_grid_layout")
        self.stock_grid_layout.setSpacing(10)

        for i in range(0, self.stock_display_per_page + 1):
            stock_ui_list_dict = {}
            stock_ui_list_dict["stock_name"] = QtWidgets.QLabel(self.widget)
            stock_ui_list_dict["up_down_value"] = QtWidgets.QLabel(self.widget)
            stock_ui_list_dict["up_down_percent"] = QtWidgets.QLabel(self.widget)
            stock_ui_list_dict["value"] = QtWidgets.QLabel(self.widget)
            stock_ui_list_dict["notify"] = QtWidgets.QCheckBox("notify", self.widget)
            stock_ui_list_dict["notify"].setTristate(False)
            stock_ui_list_dict["limit"] = QtWidgets.QLineEdit(self.widget)
            stock_ui_list_dict["upper"] = QtWidgets.QLineEdit(self.widget)
            stock_ui_list_dict["lower"] = QtWidgets.QLineEdit(self.widget)
            stock_ui_list_dict["valid_cnt"] = 0
            self.stock_grid_layout.addWidget(stock_ui_list_dict["stock_name"], i, 0, 1, 1)
            self.stock_grid_layout.addWidget(stock_ui_list_dict["up_down_value"], i, 1, 1, 1)
            self.stock_grid_layout.addWidget(stock_ui_list_dict["up_down_percent"], i, 2, 1, 1)
            self.stock_grid_layout.addWidget(stock_ui_list_dict["value"], i, 3, 1, 1)
            self.stock_grid_layout.addWidget(stock_ui_list_dict["notify"], i, 4, 1, 1)
            self.stock_grid_layout.addWidget(stock_ui_list_dict["limit"], i, 5, 1, 1)
            self.stock_grid_layout.addWidget(stock_ui_list_dict["upper"], i, 6, 1, 1)
            self.stock_grid_layout.addWidget(stock_ui_list_dict["lower"], i, 7, 1, 1)
            self.stock_list.append(stock_ui_list_dict)
        self.stock_list[0]["limit"].textChanged.connect(self.stock_line_edit_changed)

        columnMinimumWidth = 300
        self.stock_grid_layout.setColumnMinimumWidth(0, columnMinimumWidth)
        self.stock_grid_layout.setColumnMinimumWidth(1, columnMinimumWidth)
        self.stock_grid_layout.setColumnMinimumWidth(2, columnMinimumWidth)
        self.stock_grid_layout.setColumnMinimumWidth(3, columnMinimumWidth)
        self.stock_grid_layout.setColumnMinimumWidth(4, columnMinimumWidth)
        self.stock_grid_layout.setColumnMinimumWidth(5, columnMinimumWidth)
        self.stock_grid_layout.setColumnMinimumWidth(6, columnMinimumWidth)


        self.stock_grid_layout.setRowMinimumHeight(0, 10)
        self.stock_grid_layout.setRowMinimumHeight(1, 10)
        self.stock_grid_layout.setRowMinimumHeight(2, 10)
        self.stock_grid_layout.setRowMinimumHeight(3, 10)
        self.stock_grid_layout.setRowMinimumHeight(4, 10)
        self.stock_grid_layout.setRowMinimumHeight(5, 10)
        self.stock_grid_layout.setRowMinimumHeight(6, 10)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 430, 592, 351))
        self.widget.setObjectName("widget")

        self.compare_grid_layout = QtWidgets.QGridLayout(self.widget)
        self.compare_grid_layout.setContentsMargins(10, 10, 10, 10)
        self.compare_grid_layout.setObjectName("compare_grid_layout")
        self.compare_grid_layout.setSpacing(10)

        for i in range(0, self.compare_per_page):
            compare_ui_list_dict = {}
            compare_ui_list_dict["stock_name_1"] = QtWidgets.QLabel(self.widget)
            compare_ui_list_dict["up_down_percent_1"] = QtWidgets.QLabel(self.widget)
            compare_ui_list_dict["stock_name_2"] = QtWidgets.QLabel(self.widget)
            compare_ui_list_dict["up_down_percent_2"] = QtWidgets.QLabel(self.widget)
            compare_ui_list_dict["notify"] = QtWidgets.QCheckBox("notify", self.widget)
            compare_ui_list_dict["notify"].setTristate(False)
            compare_ui_list_dict["limit"] = QtWidgets.QLineEdit(self.widget)
            compare_ui_list_dict["valid_cnt"] = 0
            self.compare_grid_layout.addWidget(compare_ui_list_dict["stock_name_1"], i, 0, 1, 1)
            self.compare_grid_layout.addWidget(compare_ui_list_dict["up_down_percent_1"], i, 1, 1, 1)
            self.compare_grid_layout.addWidget(compare_ui_list_dict["stock_name_2"], i, 2, 1, 1)
            self.compare_grid_layout.addWidget(compare_ui_list_dict["up_down_percent_2"], i, 3, 1, 1)
            self.compare_grid_layout.addWidget(compare_ui_list_dict["notify"], i, 4, 1, 1)
            self.compare_grid_layout.addWidget(compare_ui_list_dict["limit"], i, 5, 1, 1)
            self.compare_list.append(compare_ui_list_dict)
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_compare_notify_value(self, name1, name2):
        if len(self.compare_list) != 0:
            for i in range(0, len(self.compare_list)):
                if (name1 == self.compare_list[i]["stock_name_1"].text()) and (name2 == self.compare_list[i]["stock_name_2"].text()):
                    return self.compare_list[i]["notify"].isChecked()
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
                    return self.zs_list[i]["notify"].isChecked()
        return None

    def get_zs_limit_value(self, name):
        if len(self.zs_list) != 0:
            for i in range(0, len(self.zs_list)):
                if name == self.zs_list[i]["stock_name"].text():
                    return self.zs_list[i]["limit"].text()
        return None

    def get_upper_value_by_name(self, name):
        if len(self.stock_list) != 0:
            for i in range(0, len(self.stock_list)):
                if name == self.stock_list[i]["stock_name"].text():
                    return self.stock_list[i]["upper"].text()
        return None

    def get_lower_value_by_name(self, name):
        if len(self.stock_list) != 0:
            for i in range(0, len(self.stock_list)):
                if name == self.stock_list[i]["stock_name"].text():
                    return self.stock_list[i]["lower"].text()
        return None

    def get_notify_value_by_name(self, name):
        if len(self.stock_list) != 0:
            #print("get notify of", name)
            for i in range(0, len(self.stock_list)):
                if name == self.stock_list[i]["stock_name"].text():
                    #print("find notify of same name", self.stock_list[i]["stock_name"].text(), self.stock_list[i]["notify"].isChecked())
                    return self.stock_list[i]["notify"].isChecked()
        return None

    def get_limit_value_by_name(self, name):
        if len(self.stock_list) != 0:
            for i in range(0, len(self.stock_list)):
                if name == self.stock_list[i]["stock_name"].text():
                    return self.stock_list[i]["limit"].text()
        return None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.restart_button.setText(_translate("MainWindow", "restart"))
        self.save_config_button.setText(_translate("MainWindow", "saveConfig"))
        MainWindow.setWindowTitle(_translate("MainWindow", "qyh_stock_programme"))

    def update_compare_stock_info(self, compare_update_info):
        stock_len = len(compare_update_info)
        len_ui_list = len(self.compare_list)
        for i in range(0, stock_len):
            found = 0
            for j in range(0, len_ui_list):
                if (self.compare_list[j]["stock_name_1"].text() == compare_update_info[i]["stock_name_1"]) and (self.compare_list[j]["stock_name_2"].text() == compare_update_info[i]["stock_name_2"]):
                    self.compare_list[j]["up_down_percent_1"].setText(compare_update_info[i]["up_down_percent_1"])
                    self.compare_list[j]["up_down_percent_2"].setText(compare_update_info[i]["up_down_percent_2"])
                    if "notify" in compare_update_info[i].keys():
                            self.compare_list[j]["notify"].setChecked(compare_update_info[i]["notify"])
                    if "limit" in compare_update_info[i].keys():
                        self.compare_list[j]["limit"].setText(compare_update_info[i]["limit"])
                    if "color" in compare_update_info[i].keys():
                        self.compare_list[j]["stock_name_1"].setStyleSheet('color:red;background-color:blue')
                    else:
                        self.compare_list[j]["stock_name_1"].setStyleSheet('')
                    found = 1
                    self.compare_list[j]["valid_cnt"] = self.valid_cnt
                    break
            if found == 0:#can not find a name match the compare_update_info, add a new one
                self.compare_list[self.valid_compare_cnt]["stock_name_1"].setText(compare_update_info[i]["stock_name_1"])
                self.compare_list[self.valid_compare_cnt]["up_down_percent_1"].setText(compare_update_info[i]["up_down_percent_1"])
                self.compare_list[self.valid_compare_cnt]["stock_name_2"].setText(compare_update_info[i]["stock_name_2"])
                self.compare_list[self.valid_compare_cnt]["up_down_percent_2"].setText(compare_update_info[i]["up_down_percent_2"])
                if "notify" in compare_update_info[i].keys():
                        self.compare_list[self.valid_compare_cnt]["notify"].setChecked(compare_update_info[i]["notify"])
                if "limit" in compare_update_info[i].keys():
                    self.compare_list[self.valid_compare_cnt]["limit"].setText(compare_update_info[i]["limit"])
                self.compare_list[self.valid_compare_cnt]["valid_cnt"] = self.valid_cnt
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

    def update_zs_stock_info(self, zs_update_info):
        stock_len = len(zs_update_info)
        len_ui_list = len(self.zs_list)
        for i in range(0, stock_len):
            found = 0
            for j in range(0, len_ui_list):
                if (self.zs_list[j]["stock_name"].text() == zs_update_info[i]["stock_name"]):
                    self.zs_list[j]["value"].setText(zs_update_info[i]["value"])
                    self.zs_list[j]["stock_name"].setText(zs_update_info[i]["stock_name"])
                    #self.zs_list[i]["up_down_value"].setText(zs_update_info[i]["up_down_value"])
                    self.zs_list[j]["up_down_percent"].setText(zs_update_info[i]["up_down_percent"])
                    if "notify" in zs_update_info[i].keys():
                        #print("noitfy in keys, and set the checkState",stock_info[i]["stock_name"], stock_info[i]["notify"])
                        self.zs_list[j]["notify"].setChecked(zs_update_info[i]["notify"])
                    if "limit" in zs_update_info[i].keys():
                        self.zs_list[j]["limit"].setText(zs_update_info[i]["limit"])
                    if "color" in zs_update_info[i].keys():
                        self.zs_list[j]["stock_name"].setStyleSheet('color:red;background-color:blue')
                    else:
                        self.zs_list[j]["stock_name"].setStyleSheet('')
                    found = 1
                    self.zs_list[j]["valid_cnt"] = self.valid_cnt
                    break
            if found == 0:#can not find a name match the stock_info, add a new one
                self.zs_list[self.valid_zs_cnt]["stock_name"].setText(zs_update_info[i]["stock_name"])
                self.zs_list[self.valid_zs_cnt]["up_down_percent"].setText(zs_update_info[i]["up_down_percent"])
                self.zs_list[self.valid_zs_cnt]["value"].setText(zs_update_info[i]["value"])
                if "notify" in zs_update_info[i].keys():
                        self.zs_list[self.valid_zs_cnt]["notify"].setChecked(zs_update_info[i]["notify"])
                if "limit" in zs_update_info[i].keys():
                    self.zs_list[self.valid_zs_cnt]["limit"].setText(zs_update_info[i]["limit"])
                self.zs_list[self.valid_zs_cnt]["valid_cnt"] = self.valid_cnt
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

    def stock_line_edit_changed(self, text_change):
        pass

    def update_stock_info(self, stock_update_info):
        stock_len = len(stock_update_info)
        len_ui_list = len(self.stock_list)
        for i in range(0, stock_len):
            found = 0
            for j in range(0, len_ui_list):
                if (self.stock_list[j]["stock_name"].text() == stock_update_info[i]["stock_name"]):
                    self.stock_list[j]["value"].setText(stock_update_info[i]["value"])
                    self.stock_list[j]["stock_name"].setText(stock_update_info[i]["stock_name"])
                    self.stock_list[i]["up_down_value"].setText(stock_update_info[i]["up_down_value"])
                    self.stock_list[j]["up_down_percent"].setText(stock_update_info[i]["up_down_percent"])
                    if "notify" in stock_update_info[i].keys():
                        self.stock_list[j]["notify"].setChecked(stock_update_info[i]["notify"])
                    if "limit" in stock_update_info[i].keys():
                        self.stock_list[j]["limit"].setText(stock_update_info[i]["limit"])
                    if "upper" in stock_update_info[i].keys():
                        self.stock_list[j]["upper"].setText(stock_update_info[i]["upper"])
                    if "lower" in stock_update_info[i].keys():
                        self.stock_list[j]["lower"].setText(stock_update_info[i]["lower"])
                    if "color" in stock_update_info[i].keys():
                        self.stock_list[j]["stock_name"].setStyleSheet('color:red;background-color:blue')
                    else:
                        self.stock_list[j]["stock_name"].setStyleSheet('')
                    found = 1
                    self.stock_list[j]["valid_cnt"] = self.valid_cnt
                    break
            if found == 0:#can not find a name match the stock_update_info, add a new one
                self.stock_list[self.valid_stock_cnt]["stock_name"].setText(stock_update_info[i]["stock_name"])
                self.stock_list[self.valid_stock_cnt]["up_down_percent"].setText(stock_update_info[i]["up_down_percent"])
                self.stock_list[self.valid_stock_cnt]["value"].setText(stock_update_info[i]["value"])
                self.stock_list[self.valid_stock_cnt]["up_down_value"].setText(stock_update_info[i]["up_down_value"])
                self.stock_list[self.valid_stock_cnt]["value"].setText(stock_update_info[i]["value"])
                self.stock_list[self.valid_stock_cnt]["valid_cnt"] = self.valid_cnt
                if "notify" in stock_update_info[i].keys():
                        self.stock_list[self.valid_stock_cnt]["notify"].setChecked(stock_update_info[i]["notify"])
                if "limit" in stock_update_info[i].keys():
                    self.stock_list[self.valid_stock_cnt]["limit"].setText(stock_update_info[i]["limit"])
                if "upper" in stock_update_info[i].keys():
                        self.stock_list[self.valid_stock_cnt]["upper"].setText(stock_update_info[i]["upper"])
                if "lower" in stock_update_info[i].keys():
                    self.stock_list[self.valid_stock_cnt]["lower"].setText(stock_update_info[i]["lower"])
                self.valid_stock_cnt = self.valid_stock_cnt + 1
        for i in range(0, len_ui_list):
            if self.stock_list[i]["valid_cnt"] > 0:
                self.stock_list[i]["valid_cnt"] = self.stock_list[i]["valid_cnt"] - 1
            if self.stock_list[i]["valid_cnt"] > 0:
                can_see = True
            else:
                can_see = False
            self.stock_list[i]["value"].setVisible(can_see)
            self.stock_list[i]["stock_name"].setVisible(can_see)
            self.stock_list[i]["up_down_value"].setVisible(can_see)
            self.stock_list[i]["up_down_percent"].setVisible(can_see)
            self.stock_list[i]["notify"].setVisible(can_see)
            self.stock_list[i]["limit"].setVisible(can_see)
            self.stock_list[i]["upper"].setVisible(can_see)
            self.stock_list[i]["lower"].setVisible(can_see)

    def save_config_to_txt(self):
        len_ui_list = len(self.stock_list)
        save_stock_txt_str = None
        for i in range(0, self.valid_stock_cnt):
            if save_stock_txt_str == None:
                save_stock_txt_str = self.stock_list[i]["stock_name"].text()
            else:
                save_stock_txt_str = save_stock_txt_str + self.stock_list[i]["stock_name"].text()
            if self.stock_list[i]["notify"].isChecked():
                save_stock_txt_str = save_stock_txt_str + " " + "1"
            else:
                save_stock_txt_str = save_stock_txt_str + " " + "0"
            if self.stock_list[i]["limit"].text():
                save_stock_txt_str = save_stock_txt_str + " " + self.stock_list[i]["limit"].text()
            else:
                save_stock_txt_str = save_stock_txt_str + " " + "0"
            if self.stock_list[i]["upper"].text():
                save_stock_txt_str = save_stock_txt_str + " " + self.stock_list[i]["upper"].text()
            else:
                save_stock_txt_str = save_stock_txt_str + " " + "0"
            if self.stock_list[i]["lower"].text():
                save_stock_txt_str = save_stock_txt_str + " " + self.stock_list[i]["lower"].text()
            else:
                save_stock_txt_str = save_stock_txt_str + " " + "0"
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
            if self.zs_list[i]["notify"].isChecked():
                save_stock_txt_str = save_stock_txt_str + " " + "1"
            else:
                save_stock_txt_str = save_stock_txt_str + " " + "0"
            if self.zs_list[i]["limit"].text():
                save_stock_txt_str = save_stock_txt_str + " " + self.zs_list[i]["limit"].text()
            else:
                save_stock_txt_str = save_stock_txt_str + " " + "0"
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
            if self.compare_list[i]["notify"].isChecked():
                save_stock_txt_str = save_stock_txt_str + " " + "1"
            else:
                save_stock_txt_str = save_stock_txt_str + " " + "0"
            if self.compare_list[i]["limit"].text():
                save_stock_txt_str = save_stock_txt_str + " " + self.compare_list[i]["limit"].text()
            else:
                save_stock_txt_str = save_stock_txt_str + " " + "0"
            if i != self.valid_compare_cnt - 1:
                save_stock_txt_str = save_stock_txt_str + "\n"
        f = open("monitor_pool.txt", "w")
        f.write(save_stock_txt_str)
        f.close()
        self.c.save_signal_slot("test call")

