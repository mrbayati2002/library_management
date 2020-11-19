#!/usr/bin/python3

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import os
import os.path
from PyQt5.uic import loadUiType

ui, _ = loadUiType('main.ui')

class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUi()
        self.Handle_Menu_Buttons()


    def InitUi(self):
        self.tab_today.tabBar().setVisible(False)

    def Handle_Menu_Buttons(self):
        self.btn_quit.clicked.connect(self.Quit)

    def Quit(self):
        sys.exit()


def main():
    App = QApplication(sys.argv)
    windows = MainApp()
    windows.show()
    App.exec_()

if __name__ == '__main__':
    main()