# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class EditWindow():
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(663, 600)
		self.mwindow = MainWindow
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		
		self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.textEdit.setGeometry(QtCore.QRect(30, 20, 451, 511))
		self.textEdit.setObjectName("textEdit")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(510, 50, 99, 27))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.open_file)
	
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(510, 120, 99, 27))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(510, 190, 99, 27))
		self.pushButton_3.setObjectName("pushButton_3")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 25))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	def open_file(self):
		#fileName = QFileDialog.getOpenFileName(self, tr("Open File"),"./",tr("TextFile (*.txt)"))
		fileName = QFileDialog.getOpenFileName(self.mwindow, "Open File","./", "*.txt")
		if fileName == None:
			print("please select a file")
			return
		else:
			print("file select is ",  fileName[0])
			self.textEdit.setText
			
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "PushButton"))
		self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
		self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
