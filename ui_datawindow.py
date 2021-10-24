# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datawindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DataWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 478)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.pushButton = QPushButton(self.centralWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 120, 281, 61))
        self.textBrowser = QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 220, 661, 131))
        self.lineEdit = QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 20, 211, 41))
        self.lineEdit_2 = QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(400, 20, 211, 41))
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 55, 16))
        self.label_2 = QLabel(self.centralWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 30, 55, 16))
        self.lineEdit_3 = QLineEdit(self.centralWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(0, 360, 561, 22))
        self.pushButton_2 = QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(570, 360, 81, 21))
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

