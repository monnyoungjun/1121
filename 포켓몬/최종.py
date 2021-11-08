import sys
from random import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic  # ui 불러오기 위해 필요
from functools import partial  # 화면 정렬하기 위해 필요함!!
from PyQt5 import QtCore, QtWidgets  # 이게 있어야 아래 정렬 함수가 제대로 활성화된다!!
import pyautogui
import pyperclip
import sqlite3
import pymysql

page1 = uic.loadUiType("../ssss/bonsa.ui")[0]

class MainWindow(QMainWindow, page1):  #ui1
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def kkkbt(self):
        import pymysql

        conn = pymysql.connect(host='10.10.21.101', port=3306, user='root'
                               , password='shs5481', db='branch_main', charset='utf8', autocommit=True)
        cursor = conn.cursor()
        sql = 'select menu from order_history'
        cursor.execute(sql)
        result = cursor.fetchall()

        self.textBrowser.clear()

        for i in result:
            print(i)

            self.textBrowser.append("{}".format(i))


        print(result)


        conn.commit()
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()
