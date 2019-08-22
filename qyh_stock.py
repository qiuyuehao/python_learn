# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qyh_stock.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
	display_per_page = 7
	zs_display_per_page = 5
	ui_list = []
	zs_list = []
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("qyh_stock_win")
		MainWindow.resize(778, 851)
		MainWindow.setWindowIcon(QIcon('sea.jpg'))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(120, 590, 89, 25))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(580, 590, 89, 25))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(350, 590, 89, 25))
		self.pushButton_3.setObjectName("pushButton_3")
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
			self.gridLayout.addWidget(ui_list_dict["stock_name"], 0, i, 1, 1)
			self.gridLayout.addWidget(ui_list_dict["up_down_percent"], 1, i, 1, 1)
			self.gridLayout.addWidget(ui_list_dict["value"], 2, i, 1, 1)
			self.gridLayout.addWidget(ui_list_dict["notify"], 3, i, 1, 1)
			self.gridLayout.addWidget(ui_list_dict["limit"], 4, i, 1, 1)
			self.zs_list.append(ui_list_dict)
		self.widget1 = QtWidgets.QWidget(self.centralwidget)
		self.widget1.setGeometry(QtCore.QRect(50, 180, 592, 351))
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
			self.gridLayout_3.addWidget(ui_list_dict["stock_name"], i, 0, 1, 1)
			self.gridLayout_3.addWidget(ui_list_dict["up_down_value"], i, 1, 1, 1)
			self.gridLayout_3.addWidget(ui_list_dict["up_down_percent"], i, 2, 1, 1)
			self.gridLayout_3.addWidget(ui_list_dict["value"], i, 3, 1, 1)
			self.gridLayout_3.addWidget(ui_list_dict["notify"], i, 4, 1, 1)
			self.gridLayout_3.addWidget(ui_list_dict["limit"], i, 5, 1, 1)
			self.gridLayout_3.addWidget(ui_list_dict["upper"], i, 6, 1, 1)
			self.gridLayout_3.addWidget(ui_list_dict["lower"], i, 7, 1, 1)		
			self.ui_list.append(ui_list_dict)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	def get_zs_notify_value(self, line):
		a = self.zs_list[line]["notify"].text()
		return a
	def get_zs_limit_value(self, line):
		a = self.zs_list[line]["limit"].text()
		return a
	def get_upper_value(self, line):
		return self.ui_list[line]["upper"].text()
	def get_lower_value(self, line):
		return self.ui_list[line]["lower"].text()
	def get_notify_value(self, line):
		return self.ui_list[line]["notify"].text()
	def get_limit_value(self, line):
		return self.ui_list[line]["limit"].text()
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		self.pushButton.setText(_translate("MainWindow", "start"))
		self.pushButton_2.setText(_translate("MainWindow", "stop"))
		self.pushButton_3.setText(_translate("MainWindow", "edit"))
		MainWindow.setWindowTitle(_translate("MainWindow", "qyh_stock_win"))
	def update_zs_stock_info(self, stock_info):
		stock_len = len(stock_info)
		len_ui_list = len(self.zs_list)
		for i in range(0, stock_len):
			self.zs_list[i]["value"].setText(stock_info[i]["value"])
			self.zs_list[i]["stock_name"].setText(stock_info[i]["stock_name"])
			#self.zs_list[i]["up_down_value"].setText(stock_info[i]["up_down_value"])
			self.zs_list[i]["up_down_percent"].setText(stock_info[i]["up_down_percent"])
			if "notify" in stock_info[i].keys():		
				self.zs_list[i]["notify"].setText(stock_info[i]["notify"])
			if "limit" in stock_info[i].keys():			
				self.zs_list[i]["limit"].setText(stock_info[i]["limit"])
		i = 0
		while i < stock_len:
			self.zs_list[i]["value"].setVisible(True)
			self.zs_list[i]["stock_name"].setVisible(True)
			#self.zs_list[i]["up_down_value"].setVisible(True)
			self.zs_list[i]["up_down_percent"].setVisible(True)
			self.zs_list[i]["notify"].setVisible(True)
			self.zs_list[i]["limit"].setVisible(True)
			i = i + 1
		i = stock_len
		while i < len_ui_list:
			self.zs_list[i]["value"].setVisible(False)
			self.zs_list[i]["stock_name"].setVisible(False)
			#self.ui_list[i]["up_down_value"].setVisible(False)
			self.zs_list[i]["up_down_percent"].setVisible(False)
			self.zs_list[i]["notify"].setVisible(False)
			self.zs_list[i]["limit"].setVisible(False)
			i = i + 1
	def update_stock_info(self, stock_info):
		stock_len = len(stock_info)
		len_ui_list = len(self.ui_list)
		for i in range(0, stock_len):
			self.ui_list[i]["value"].setText(stock_info[i]["value"])
			self.ui_list[i]["stock_name"].setText(stock_info[i]["stock_name"])
			self.ui_list[i]["up_down_value"].setText(stock_info[i]["up_down_value"])
			self.ui_list[i]["up_down_percent"].setText(stock_info[i]["up_down_percent"])
			if "notify" in stock_info[i].keys():
				self.ui_list[i]["notify"].setText(stock_info[i]["notify"])
			if "limit" in stock_info[i].keys():
				self.ui_list[i]["limit"].setText(stock_info[i]["limit"])
			if "upper" in stock_info[i].keys():
				self.ui_list[i]["upper"].setText(stock_info[i]["upper"])
			if "lower" in stock_info[i].keys():
				self.ui_list[i]["lower"].setText(stock_info[i]["lower"])
		i = 0
		while i < stock_len:
			self.ui_list[i]["value"].setVisible(True)
			self.ui_list[i]["stock_name"].setVisible(True)
			self.ui_list[i]["up_down_value"].setVisible(True)
			self.ui_list[i]["up_down_percent"].setVisible(True)
			self.ui_list[i]["notify"].setVisible(True)
			self.ui_list[i]["limit"].setVisible(True)
			self.ui_list[i]["upper"].setVisible(True)
			self.ui_list[i]["lower"].setVisible(True)
			i = i + 1
		i = stock_len
		while i < len_ui_list:
			self.ui_list[i]["value"].setVisible(False)
			self.ui_list[i]["stock_name"].setVisible(False)
			self.ui_list[i]["up_down_value"].setVisible(False)
			self.ui_list[i]["up_down_percent"].setVisible(False)
			self.ui_list[i]["notify"].setVisible(False)
			self.ui_list[i]["limit"].setVisible(False)
			self.ui_list[i]["upper"].setVisible(False)
			self.ui_list[i]["lower"].setVisible(False)
			i = i + 1