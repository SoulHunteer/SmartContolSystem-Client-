import sys
import socket
from threading import Thread

import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow
from ui_settingswindow import Ui_SettingsWindow
from ui_stat import Ui_StatWindow
from ui_datawindow import Ui_DataWindow
from ui_newtab import Ui_NewTab


class NewTabMenu(QMainWindow):
    def __init__(self, parent=None):
        super(NewTabMenu, self).__init__(parent)
        self.ui = Ui_NewTab()
        self.ui.setupUi(self)
        self.main = MainWindow()
        self.setWindowTitle('Добавление устройства')
        self.newtabname = self.ui.lineEdit.text()
        print(self.newtabname)
        self.ui.pushButton.clicked.connect(self.NewTabName)
        self.ui.pushButton_2.clicked.connect(self.close)

    def NewTabName(self):
        print(self.newtabname)




class SettingsWindow(QMainWindow):
    def __init__(self, currentDevice, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.currentDevice = currentDevice
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Панель управления настройками для '{self.currentDevice}'")


class DataWindow(QMainWindow):
    def __init__(self, currentDevice, parent=None):
        super(DataWindow, self).__init__(parent)
        self.currentDevice = currentDevice
        self.ui = Ui_DataWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Обмен данными с '{self.currentDevice}'")
        default_ip = 'localhost'
        default_port = '8000'
        self.ui.lineEdit.setText(default_ip)
        self.ui.lineEdit_2.setText(default_port)
        self.ui.pushButton.clicked.connect(self.clientSettings)

    def clientSettings(self):
        self.MyClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tupleConnect = (self.ui.lineEdit.text(), int(self.ui.lineEdit_2.text()))
            self.MyClient.connect(tupleConnect)
        except ValueError as e:
            self.ui.textBrowser.append(str(e))
            self.ui.textBrowser.append('Please, check your ip and port!')
        except ConnectionError as e:
            self.ui.textBrowser.append(str(e))
        except TimeoutError as e:
            self.ui.textBrowser.append(str(e))
        serverdata = 'Server say: ' + self.MyClient.recv(8192).decode('utf-8')
        self.ui.textBrowser.append(serverdata)
        self.ui.pushButton_2.clicked.connect(self.sendButton)

    def sendButton(self):
        self.MyClient.send(self.ui.lineEdit_3.text().encode('utf-8'))
        self.ui.lineEdit_3.clear()


class StatWindow(QMainWindow):
    def __init__(self, currentDevice, parent=None):
        super(StatWindow, self).__init__(parent)
        self.currentDevice = currentDevice
        self.ui = Ui_StatWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Статистика для '{self.currentDevice}'")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.newtabname = ''
        self.index = self.ui.tabWidget.currentIndex()
        self.currentDevice = self.ui.tabWidget.tabText(self.index)
        self.ui.pushButton.clicked.connect(self.SetingsButtonEvent)
        self.ui.pushButton_2.clicked.connect(self.DataButtonEvent)
        self.ui.pushButton_3.clicked.connect(self.StatisicButtonEvent)
        self.ui.pushButton_4.clicked.connect(self.NewDeviceEvent)
        '''
        self.ui.pushButton_5.clicked.connect(self.StatisicButtonEvent)
        self.ui.pushButton_6.clicked.connect(self.SetingsButtonEvent)
        self.ui.pushButton_7.clicked.connect(self.DataButtonEvent)
        self.ui.pushButton_8.clicked.connect(self.StatisicButtonEvent)
        self.ui.pushButton_9.clicked.connect(self.SetingsButtonEvent)
        '''


    def SetingsButtonEvent(self):
        self.index = self.ui.tabWidget.currentIndex()
        self.currentDevice = self.ui.tabWidget.tabText(self.index)
        self.getSettingsWindow = SettingsWindow(currentDevice=self.currentDevice)
        self.getSettingsWindow.show()

    def StatisicButtonEvent(self):
        self.index = self.ui.tabWidget.currentIndex()
        self.currentDevice = self.ui.tabWidget.tabText(self.index)
        self.getStatWindow = DataWindow(currentDevice=self.currentDevice)
        self.getStatWindow.show()

    def DataButtonEvent(self):
        self.index = self.ui.tabWidget.currentIndex()
        self.currentDevice = self.ui.tabWidget.tabText(self.index)
        self.getDataWindow = StatWindow(currentDevice=self.currentDevice)
        self.getDataWindow.show()

    def NewDeviceEvent(self):
        self.getNewNameTab = NewTabMenu()
        self.getNewNameTab.show()
        self.ui.tabWidget.addTab(QWidget(), 'Waiting input...')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
