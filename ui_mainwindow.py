# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Smart control System")
        MainWindow.resize(657, 478)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 661, 431))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 250, 201, 81))
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 50, 201, 81))
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 150, 201, 81))
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(-20, 10, 681, 31))
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 310, 120, 80))
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(490, 360, 161, 41))
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Smart control System", u"Smart control System", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0442\u0441\u0442\u0438\u043a\u0430", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043c\u0435\u043d \u0434\u0430\u043d\u043d\u044b\u043c\u0438", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#55ff7f;\">Smart Control System</span></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e 1", None))
    # retranslateUi

