# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newtab.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_NewTab(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(388, 178)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.lineEdit = QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 40, 241, 22))
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 221, 21))
        self.pushButton = QPushButton(self.centralWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 90, 93, 28))
        self.pushButton_2 = QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 90, 93, 28))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

