import random
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import re
import pyautogui #메시지박스 쓰기 위한 라이브러리
import socket
import datetime, time
now = datetime.datetime.now()
now = now.strftime("%Y.%m.%d %H:%M:%S")

import sqlite3
import pandas, numpy
# conn = sqlite3.connect("../수업실습/membershipDB.db", isolation_level=None)
# # conn.row_factory = sqlite3.Row
# cur = conn.cursor()
ip = socket.gethostbyname(socket.gethostname())

import pymysql
conn = pymysql.connect(host='192.168.0.14',port=3306,user='root'
                       ,password='shs5481',db='branch_main',charset='utf8', autocommit=True)
cur = conn.cursor()
conn2 = pymysql.connect(host='192.168.0.14',port=3306,user='root'
                       ,password='shs5481',db='branch_suwan',charset='utf8', autocommit=True)
cur2 = conn2.cursor()

one = 'main.ui'
two = 'pay.ui'
loginUI = 'login.ui'

class window2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(two, self)
        self.pushButton_16.clicked.connect(self.paydone) #카드결제
        self.pushButton_15.clicked.connect(self.cashpay) #현금결제
    def paydone(self): #카드결제 주문
        pyautogui.alert("주문이 완료되었습니다.")
        self.lista = re.findall(r'\d+', self.textBrowser_2.toPlainText())  # 숫자추출함수 #가격에서 숫자만추출
        self.listb = self.textBrowser.toPlainText().split('\n') # 주문내역 리스트
        print(self.listb)
        self.branch = self.label.text()

        self.quantity= [] # 개수 리스트
        for i in range(len(self.listb)):
            self.quantity2 = re.findall(r'\d+', self.listb[i])
            self.quantity.append(int(self.quantity2[0]))
        # print(self.quantity)
        self.menu =[] #메뉴 리스트
        for i in range(len(self.listb)):
            self.menu2 = self.listb[i].split(' ')
            print(self.menu2[0])
            self.menu.append(self.menu2[0])
        print(self.menu)
        for i in range(len(self.listb)):
            cur.execute("INSERT INTO order_history(id,time,menu,quantity,cost,PM,branch) VALUES('{}','{}','{}','{}',{},'card','{}')"
                        .format(self.label_9.text(),now,self.menu[i],self.quantity[i],int(self.lista[0]),self.branch))
    def cashpay(self): #현금결제
        pyautogui.alert("현금결제는 불가능합니다.")
        # self.lista = re.findall(r'\d+', self.textBrowser_2.toPlainText())  # 숫자추출함수 #가격에서 '원'제거한 값
        # self.listb = self.textBrowser.toPlainText().split('\n')  # 주문내역 리스트
        # self.branch = self.label.text()
        # if self.textEdit.toPlainText().isdigit() == False: #숫자가 아니면
        #     pyautogui.alert("돈을 넣어주세요.")
        # elif int(self.textEdit.toPlainText()) == int(self.lista[0]):
        #     print(self.textBrowser.toPlainText())
        #     pyautogui.alert("주문이 완료되었습니다.")
        #     for i in range(len(self.listb)):
        #         cur.execute("INSERT INTO order_history(id,time,menu,cost,PM,branch) VALUES('{}','{}','{}',{},'card','{}')"
        #             .format(self.label_9.text(), now, self.listb[i], int(self.lista[0]), self.branch))
        # elif int(self.textEdit.toPlainText()) >= int(self.lista[0]):
        #     pyautogui.alert("주문이 완료되었습니다.\n거스름돈 {}원 가져가세요.".format(int(self.textEdit.toPlainText())-int(self.lista[0])))
        #     for i in range(len(self.listb)):
        #         cur.execute("INSERT INTO order_history(id,time,menu,cost,PM,branch) VALUES('{}','{}','{}',{},'card','{}')"
        #             .format(self.label_9.text(), now, self.listb[i], int(self.lista[0]), self.branch))
        # else:
        #     pyautogui.alert("잔액이 부족합니다.")

class window1(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(one, self)

        #self.tabWiget.setStyleSheet("QTabBar:tab{"" height: 100px; width:410px;""}")

        # cur.execute('SELECT branch FROM branch_list') # WHERE id = "{}"'.format(self.label_9.text()))
        # a = cur.fetchall()
        # for i in range(len(a)):
        #     self.comboBox.addItem(a[i][0])

        self.ame = 0
        self.latte = 0
        self.moca = 0
        self.green = 0
        self.jamon = 0
        self.price = 0

        self.window2 = window2() # 페이지 2번에 값을 넘기기 위해 선언한 것

        # self.label.setStyleSheet('image:url(head.png);')
        # self.pushButton.setStyleSheet('image:url(ame3.jpg);')
        # self.pushButton_2.setStyleSheet('image:url(doll1.jpg);')
        # self.pushButton_3.setStyleSheet('image:url(java1.jpg);')
        # self.pushButton_4.setStyleSheet('image:url(jeju1.jpg);')
        # self.pushButton_5.setStyleSheet('image:url(jamon1.jpg);')

        self.pushButton_6.clicked.connect(self.nextpage)
        self.pushButton_7.clicked.connect(self.reset)

        self.pushButton.clicked.connect(self.amef)
        self.pushButton.clicked.connect(self.orderlist)
        self.pushButton_2.clicked.connect(self.lattef)
        self.pushButton_2.clicked.connect(self.orderlist)
        self.pushButton_3.clicked.connect(self.mocaf)
        self.pushButton_3.clicked.connect(self.orderlist)
        self.pushButton_4.clicked.connect(self.greenf)
        self.pushButton_4.clicked.connect(self.orderlist)
        self.pushButton_5.clicked.connect(self.jamonf)
        self.pushButton_5.clicked.connect(self.orderlist)
        self.pushButton_8.clicked.connect(self.pw_change) #암호변경
        self.pushButton_9.clicked.connect(self.membership_withdrawal) #회원탈퇴
        self.pushButton_10.clicked.connect(self.orderlist_print) #주문기록조회

    def membership_withdrawal(self): # 회원탈퇴
        confirm = pyautogui.confirm("탈퇴를 하시면 회원정보와 주문내역이 모두 삭제됩니다. 삭제하시겠습니까?")
        if confirm == "OK":
            cur.execute("DELETE FROM member WHERE id = '{}'".format(self.label_9.text()))
            cur.execute("DELETE FROM order_history WHERE id = '{}'".format(self.label_9.text()))
            cur2.execute("DELETE FROM member WHERE id = '{}'".format(self.label_9.text()))
            cur2.execute("DELETE FROM order_history WHERE id = '{}'".format(self.label_9.text()))
            ss.show()
            self.close()

    def pw_change(self): # 비밀번호변경
        pyautogui.alert("비밀번호가 변경되었습니다.")
        cur.execute('UPDATE member SET pw = "{}" WHERE id = "{}"'.format(self.lineEdit_2.text(), self.label_9.text()))
        cur2.execute('UPDATE member SET pw = "{}" WHERE id = "{}"'.format(self.lineEdit_2.text(), self.label_9.text()))

    def orderlist_print(self): # 주문조회
        pyautogui.alert("준비중입니다.")
    #     # a = pandas.read_sql('SELECT * FROM order_history WHERE id = "{}"'.format(self.label_9.text()),conn)
    #     cur.execute('SELECT * FROM order_history WHERE id = "{}"'.format(self.label_9.text()))
    #     a = cur.fetchall()
    #     self.textBrowser_3.clear()
    #     # self.textBrowser_3.append("{}".format(a))
    #     for i in range(len(a)):
    #         self.textBrowser_3.append("{}\n{}\n{}\n{}\n" .format(a[i][1],a[i][2],a[i][3],a[i][4]))

    def reset(self):
        self.ame = 0
        self.latte = 0
        self.moca = 0
        self.green = 0
        self.jamon = 0
        self.price = 0
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.window2.textBrowser.clear()
        self.window2.textBrowser_2.clear()
    def nextpage(self): #주문하기 누르면
        #self.window2.listWidget.addItem(self.lineEdit.text()) # 값을 넘기는 것
        # self.window2.label.setText(self.comboBox.currentText())
        # self.window2.label_9.setText(self.label_9.text())
        # self.window2.show() # 페이지 전환 것
        #self.close()
        pyautogui.alert("주문이 완료되었습니다.")
        self.lista = re.findall(r'\d+', self.textBrowser_2.toPlainText())  # 숫자추출함수 #가격에서 숫자만추출
        self.listb = self.textBrowser.toPlainText().split('\n')  # 주문내역 리스트
        # print(self.listb)
        self.branch = self.comboBox.currentText()

        self.quantity = []  # 개수 리스트
        for i in range(len(self.listb)):
            self.quantity2 = re.findall(r'\d+', self.listb[i])
            self.quantity.append(int(self.quantity2[0]))
        # print(self.quantity)
        self.menu = []  # 메뉴 리스트
        for i in range(len(self.listb)):
            self.menu2 = self.listb[i].split(' ')
            print(self.menu2[0])
            self.menu.append(self.menu2[0])
        # print(self.menu)

        # cost 리스트
        self.ame_price = self.ame * 4100
        self.latte_price = self.latte * 4500
        self.moca_price = self.moca * 6500
        self.green_price = self.green * 6300
        self.jamon_price = self.jamon * 5400

        self.cost_list = []
        if self.ame > 0:
            self.cost_list.append(self.ame_price)
        if self.latte > 0:
            self.cost_list.append(self.latte_price)
        if self.moca > 0:
            self.cost_list.append(self.moca_price)
        if self.green > 0:
            self.cost_list.append(self.green_price)
        if self.jamon > 0:
            self.cost_list.append(self.jamon_price)
        # print("costlist =", self.cost_list)x

        print('aa')
        self.ss1 = random.randint(1, 9)
        print('asda')
        self.ss2 = random.randint(10, 28)
        self.ss3 = random.randint(10, 23)
        self.ss4 = random.randint(10, 59)
        self.ss5 = random.randint(10, 59)
        self.calen = ['2021.0{}.{} {}:{}:{}'.format(self.ss1,self.ss2,self.ss3,self.ss4,self.ss5)]
        print(self.calen)
        # order_history insert
        for i in range(len(self.listb)):
            cur.execute(
                "INSERT INTO order_history(id,time,menu,quantity,cost,PM,branch) VALUES('{}','{}','{}','{}',{},'card','{}')"
                .format(self.label_9.text(), self.calen[0], self.menu[i], self.quantity[i], self.cost_list[i], self.branch))
            cur2.execute(
                "INSERT INTO order_history(id,time,menu,quantity,cost,PM,branch) VALUES('{}','{}','{}','{}',{},'card','{}')"
                .format(self.label_9.text(), self.calen[0], self.menu[i], self.quantity[i], self.cost_list[i], self.branch))

    def amef(self):
        self.ame+=1
        self.price+=4100
    def lattef(self):
        self.latte += 1
        self.price += 4500
    def mocaf(self):
        self.moca += 1
        self.price += 6500
    def greenf(self):
        self.green += 1
        self.price += 6300
    def jamonf(self):
        self.jamon += 1
        self.jamon_price = self.moca * 5400
        self.price += 5400

    def orderlist(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.window2.textBrowser.clear()
        self.window2.textBrowser_2.clear()
        if self.ame>0:
            self.textBrowser.append("ame {}".format(self.ame))
            self.window2.textBrowser.append("ame {}".format(self.ame))
        if self.latte>0:
            self.textBrowser.append("latte {}".format(self.latte))
            self.window2.textBrowser.append("latte {}".format(self.latte))
        if self.moca>0:
            self.textBrowser.append("moca {}".format(self.moca))
            self.window2.textBrowser.append("moca {}".format(self.moca))
        if self.green>0:
            self.textBrowser.append("green {}".format(self.green))
            self.window2.textBrowser.append("green {}".format(self.latte))
        if self.jamon>0:
            self.textBrowser.append("jamon {}".format(self.jamon))
            self.window2.textBrowser.append("jamon {}".format(self.jamon))

        self.textBrowser_2.append("{}원".format(self.price))
        self.window2.textBrowser_2.append("{}원".format(self.price))

class login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(loginUI, self)

        # PW 가림용 문자로 표시하기
        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
        # PW 입력시만 문자로 표시 (?) , 수정 중엔 다른 문자로 표시
        # self.lineEdit_2.setEchoMode(self.lineEdit_2.PasswordEchoOnEdit)

        # self.lineEdit.setStyleSheet("background-color: rgb(121, 213, 255);")

        self.window1 = window1()
        self.pushButton.clicked.connect(self.nextpage) #로그인
        self.pushButton_2.clicked.connect(self.join) #회원가입
        self.pushButton_3.clicked.connect(self.id_check) #중복확인
        self.pushButton_4.clicked.connect(self.join_complete) #가입완료
        self.pushButton_5.clicked.connect(self.join_cancel)  #가입취소
    def join_cancel(self):
        currentpage = ss.stackedWidget.currentIndex()
        ss.stackedWidget.setCurrentIndex(currentpage - 1)
    def nextpage(self): #로그인
        id = self.lineEdit.text()
        pw = self.lineEdit_2.text()
        cur.execute("SELECT pw FROM member WHERE id = '{}'".format(id))
        result = cur.fetchall()
        try:
            if result[0][0] == pw:
                self.window1.label_9.setText(id)
                self.window1.lineEdit_2.setText(pw)
                self.window1.show()
                self.close()
            else:
                if not pw:
                    pyautogui.alert("비밀번호를 입력해주세요.")
                else:
                    pyautogui.alert("비밀번호가 틀렸습니다.")
        except:
            if not id:
                pyautogui.alert("아이디를 입력해주세요.")
            else:
                pyautogui.alert("없는 아이디입니다.")

    def join(self): #회원가입 클릭 시
        currentpage = ss.stackedWidget.currentIndex()
        ss.stackedWidget.setCurrentIndex(currentpage + 1) # stacked widget 페이지넘김
    def join_complete(self): #가입완료 클릭 시
        id = self.lineEdit_3.text()
        pw = self.lineEdit_4.text()

        id_findall = re.findall(' ', id)
        cur.execute("SELECT id FROM member WHERE id = '{}'".format(id))
        result = cur.fetchall()
        if not result: # 공백이거나 Null인 경우
            if not id: #id 입력란이 공백이거나 Null인 경우
                pyautogui.alert("아이디를 입력해주세요.")
            elif id_findall:  # 공백이거나 NULL이 아닌 경우
                pyautogui.alert("띄어쓰기는 사용하실 수 없습니다.")
            else:
                if pw:
                    cur.execute("INSERT INTO member(date,id,pw) VALUES('{}','{}','{}')".format(now, id, pw))
                    cur2.execute("INSERT INTO member(date,id,pw) VALUES('{}','{}','{}')".format(now, id, pw))
                    currentpage = ss.stackedWidget.currentIndex()
                    ss.stackedWidget.setCurrentIndex(currentpage - 1)
                else:
                    pyautogui.alert("pw를 입력해주세요.")
        else:
            if result[0][0] == id:
                pyautogui.alert("동일한 아이디가 있습니다")
    def id_check(self): # id 중복확인
        id = self.lineEdit_3.text()
        id_findall = re.findall(' ',id) #id에서 띄어쓰기 추출
        cur.execute("SELECT id FROM member WHERE id = '{}'".format(id))
        result = cur.fetchall()
        if not result:
            if not id: #id가 공백이거나 NULL인 경우
                pyautogui.alert("아이디를 입력해주세요.")
            elif id_findall: #id에서 띄어쓰기를 추출한 리스트가 공백이거나 NULL이 아닌 경우
                pyautogui.alert("띄어쓰기는 사용하실 수 없습니다.")
            else:
                pyautogui.alert("사용 가능한 아이디입니다.")
        else:
            if result[0][0] == id:
                pyautogui.alert("동일한 아이디가 있습니다")

app = QApplication(sys.argv)
ss = login()
ss.show()
app.exec_()