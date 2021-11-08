import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import re
import pyautogui
import pymysql
import sqlite3
import datetime, time

now = datetime.datetime.now()
now = now.strftime("%Y.%m.%d %H:%M:%S")

# page1 = uic.loadUi('Log.ui')[0]
# page2 = uic.loadUi('order.ui')[0]

one = "Log.ui"
two = "order.ui"

class window2(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(two, self)
        self.menu_list = []
        self.cost_list = []
        self.ame = 0
        self.latte = 0
        self.moca = 0
        self.green = 0
        self.jamon = 0
        self.price = 0

        self.order_Button.clicked.connect(self.nextpage)
        self.cancel_Button.clicked.connect(self.reset)

        self.Americano_Button.clicked.connect(self.amef)
        self.Americano_Button.clicked.connect(self.orderlist)
        self.cafelatte_Button.clicked.connect(self.lattef)
        self.cafelatte_Button.clicked.connect(self.orderlist)
        self.Mocha_Button.clicked.connect(self.mocaf)
        self.Mocha_Button.clicked.connect(self.orderlist)
        self.GreenTea_Button.clicked.connect(self.greenf)
        self.GreenTea_Button.clicked.connect(self.orderlist)
        self.aid_Button.clicked.connect(self.jamonf)
        self.aid_Button.clicked.connect(self.orderlist)

        self.msg = QMessageBox()
        self.caed_Button.clicked.connect(self.caed)
        # self.Bacm_Button.clicked.connect(self.Back)

    def caed(self):

        conn = pymysql.connect(host='10.10.21.101', port=3306, user='root'
                               , password='shs5481', db='branch_main', charset='utf8', autocommit=True)
        print("aa1")


        cur = conn.cursor()
        sql = "select * from order_history"
        cur.execute(sql)
        a = cur.fetchall()
        # conn = sqlite3.connect("test.db")
        # cur = conn.cursor()
        # self.msg.setIcon(QMessageBox.Information)
        # self.msg.setWindowTitle('MessageBox')
        # self.msg.setText("주문이 완료되었습니다.")
        # self.msg.setStandardButtons(QMessageBox.Ok)
        for i in range(len(self.menu_list)):
            cur.execute("INSERT INTO order_history(id,time,menu,quantity,cost,pm,branch) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(
            '123','2021.08.10 16:29:26', self.menu_list[i], 1, self.cost_list[i], 'card', 'suwan'))
        #

        print(a)
        conn.commit()
        conn.close()

    def reset(self):
        self.ame = 0
        self.latte = 0
        self.moca = 0
        self.green = 0
        self.jamon = 0
        self.price = 0
        self.order_Browser.clear()
        self.money_total_Browser.clear()
        self.window2.order_Browser.clear()
        self.window2.money_total_Browser.clear()

    def nextpage(self):
        print("aa")
        self.currentpage = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.currentpage + 1)
        # self.close()

    def amef(self):
        self.ame += 1
        self.price += 4100
        self.menu_list.append('ame')
        self.cost_list.append(4100)



    def lattef(self):
        self.latte += 1
        self.price += 4500
        self.menu_list.append('latte')
        self.cost_list.append(4500)

    def mocaf(self):
        self.moca += 1
        self.price += 6500
        self.menu_list.append('moca')
        self.cost_list.append(6500)

    def greenf(self):
        self.green += 1
        self.price += 6300
        self.menu_list.append('green')
        self.cost_list.append(6300)

    def jamonf(self):
        self.jamon += 1
        self.price += 5400
        self.menu_list.append('jamon')
        self.cost_list.append(5400)

    def orderlist(self):
        self.order_Browser.clear()
        self.money_total_Browser.clear()
        self.total_Browser.clear()
        self.total_money_Browser.clear()
        if self.ame > 0:
            self.order_Browser.append("아메리카노 {}잔".format(self.ame))
            self.total_Browser.append("아메리카노 {}잔".format(self.ame))


        if self.latte > 0:
            self.order_Browser.append("카페라떼 {}잔".format(self.latte))
            self.total_Browser.append("카페라떼 {}잔".format(self.latte))

        if self.moca > 0:
            self.order_Browser.append("모카프라프치노 {}잔".format(self.moca))
            self.total_Browser.append("모카프라프치노 {}잔".format(self.moca))


        if self.green > 0:
            self.order_Browser.append("녹차프라프치노 {}잔".format(self.green))
            self.total_Browser.append("녹차프라프치노 {}잔".format(self.green))


        if self.jamon > 0:
            self.order_Browser.append("자몽에이드 {}잔".format(self.jamon))
            self.total_Browser.append("자몽에이드 {}잔".format(self.jamon))


        self.money_total_Browser.append("{}원".format(self.price))
        self.total_money_Browser.append("{}".format(self.price))



class window1(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(one, self)
        self.msg = QMessageBox()
        self.window2 = window2()
        self.log_Button.clicked.connect(self.aaa)
        self.log_sginup_Button.clicked.connect(self.sginup)
        self.sginup_Button.clicked.connect(self.me)
        self.cancle_button.clicked.connect(self.me)

    def aaa(self):
        self.window2.show()
        self.close()
    def sginup (self):
        self.currentpage = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.currentpage + 1)

    def me(self):
        self.currentpage = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.currentpage - 1)

    def join(self):
        currentpage = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(currentpage + 1)

    def Back(self):
        self.currentpage = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.currentpage - 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = window1()
    myWindow.show()
    app.exec_()