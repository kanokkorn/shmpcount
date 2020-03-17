# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'untitled_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 700, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 311, 61))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 590, 251, 71))
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 700, 121, 61))
        self.pushButton_2.setTabletTracking(False)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 700, 121, 61))
        self.pushButton_3.setTabletTracking(False)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(930, 780, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 80, 811, 481))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 700, 121, 61))
        self.pushButton_4.setTabletTracking(False)
        self.pushButton_4.setAcceptDrops(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(780, 700, 121, 61))
        self.pushButton_5.setTabletTracking(False)
        self.pushButton_5.setAcceptDrops(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(850, 90, 251, 481))
        self.groupBox.setObjectName("groupBox")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(10, 60, 231, 391))
        self.listView.setObjectName("listView")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(920, 700, 121, 61))
        self.reset_btn.setTabletTracking(False)
        self.reset_btn.setAcceptDrops(False)
        self.reset_btn.setObjectName("reset_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.reset_btn.clicked.connect(self.exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CP Shrimp Counter"))
        self.pushButton.setText(_translate("MainWindow", "break"))
        self.label.setText(_translate("MainWindow", "Shrimp counting machine"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.pushButton_3.setText(_translate("MainWindow", "START"))
        self.pushButton_4.setText(_translate("MainWindow", "PUMP"))
        self.groupBox.setTitle(_translate("MainWindow", "???"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.menufile.setTitle(_translate("MainWindow", "Some menu"))

    def exit(self):
        exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())