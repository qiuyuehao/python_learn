# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *

class EditWindow():
	current_file_name = None
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
		self.pushButton_2.clicked.connect(self.save_file)
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(510, 190, 99, 27))
		self.pushButton_3.setObjectName("pushButton_3")
		self.pushButton_3.clicked.connect(self.cancle_file)
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
			print("file select is ",  fileName[0], type(fileName[0]))
			myFile = QFile(fileName[0])
			if not myFile.open(QFile.ReadOnly | QFile.Text):
				print("open file wrong", fileName[0])
				return
			self.current_file_name = fileName[0]
			self.mwindow.setWindowTitle(fileName[0])
			inf = QTextStream(myFile)
			file_content = inf.readAll()
			#print(inf.readAll(), type(inf.readAll()))
			self.textEdit.setPlainText(file_content)
			myFile.close()
	def cancle_file(self):
		self.current_file_name = None
		self.mwindow.setWindowTitle("please select a file to open")
		self.textEdit.clear()
	def save_file(self):
		myFile = QFile(self.current_file_name)
		if not myFile.open(QFile.WriteOnly | QFile.Text):
			print("open to write file wrong", fileName[0])
			return
		file_content = self.textEdit.toPlainText()
		print(file_content)
		file_content_bytes= bytes(file_content, encoding='utf-8')
		myFile.write(file_content_bytes)
		myFile.close()
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "open"))
		self.pushButton_2.setText(_translate("MainWindow", "save"))
		self.pushButton_3.setText(_translate("MainWindow", "cancle"))
