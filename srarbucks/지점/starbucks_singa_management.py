import sys
import socket
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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pandas as pd  # 데이터 프레임
import numpy as np  # 수치계산
import matplotlib.pyplot as plt  # 데이터 시각화
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys
from matplotlib.figure import Figure

# 기숙사 wifi ip : 172.16.3.235
# 전산실2(iot?) ip  : 192.168.0.66
# select만 되는 아이디 : aaa / 1234
# 마스터 아이디: root / shs5481

page1 = uic.loadUiType("singa.ui")[0]

class MainWindow(QMainWindow, page1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.change() # 스택위젯 페이지바뀔 시 다시 디비 커넥트하기 위해 설정

        self.canvas = FigureCanvas(Figure(figsize=(4, 3)))
        self.vbox = QVBoxLayout(self.label_1)
        self.vbox.addWidget(self.canvas)
        self.ax = self.canvas.figure.subplots()  # xy축 그리기

        self.lineEdit_pw_3.setEchoMode(QLineEdit.Password)

        self.pushButton_15.clicked.connect(self.nextpage)  # 로그인
        self.pushButton_1.clicked.connect(self.inquiry) # 조회1
        self.pushButton_11.clicked.connect(self.entireselect) #조회2

    def change(self): #커넥트변화
        self.currentpage = self.stackedWidget.currentIndex()
        print(self.currentpage)
        if self.currentpage == 1: #로그인페이지 #여기서는 관리자로 커넥트
            print('if문들어옴 로그인페이지')
            ip = socket.gethostbyname(socket.gethostname())
            conn = pymysql.connect(host='192.168.0.14', port=3306, user='root'
                               , password='shs5481', db='branch_main', charset='utf8', autocommit=True)
        if self.currentpage == 0: #로그인 성공 시 #여기서는 다른 아이디로 커넥트
            print('if문들어옴')
            # id = 'root'
            # pw = 'shs5481'
            id = self.lineEdit_id_3.text()
            pw = self.lineEdit_pw_3.text()
            ip = socket.gethostbyname(socket.gethostname())
            conn = pymysql.connect(host='192.168.0.14', port=3306, user=id
                                   , password=pw, db='branch_singa', charset='utf8', autocommit=True)
        self.cur = conn.cursor()
        self.setWindowTitle('singa점 관리자 프로그램')

    def nextpage(self): #로그인
        try:
            id = self.lineEdit_id_3.text()
            pw = self.lineEdit_pw_3.text()
            ip = socket.gethostbyname(socket.gethostname())
            conn = pymysql.connect(host='192.168.0.14', port=3306, user=id
                                   , password=pw, db='branch_singa', charset='utf8', autocommit=True)
            pyautogui.alert("로그인 성공.")
            myWindow.stackedWidget.setCurrentIndex(self.currentpage - 1)
            self.change()
        except:
            pyautogui.alert("다시 입력해주세요.")

    def inquiry(self): #조회1(혜솔)
        print("id=", id)
        self.branch_name = self.comboBox_1.currentText()
        print(self.branch_name)
        if self.comboBox_9.currentText() == "vip회원순":
            self.cur.execute("SELECT id,SUM(cost) FROM order_history WHERE branch LIKE '{}' GROUP BY id ORDER BY SUM(cost) desc".format(self.branch_name))
            result = self.cur.fetchall()
            df = pd.DataFrame(data=result)
            print('1',df)
            self.df_list_x = df[0].values.tolist()
            self.df_list_y = df[1].values.tolist()
        if self.comboBox_9.currentText() == "인기메뉴순":
            self.cur.execute(
                "SELECT menu,SUM(quantity) FROM order_history WHERE branch LIKE '{}' "
                "GROUP BY menu ORDER BY SUM(quantity) desc".format(self.branch_name))
            result = self.cur.fetchall()
            df = pd.DataFrame(data=result)
            self.df_list_x = df[0].values.tolist()
            self.df_list_y = df[1].values.tolist()
        self.ax.clear()
        self.ax.bar(self.df_list_x, self.df_list_y)
        self.ax.figure.canvas.draw()

    def entireselect(self): #조회2(재원)

        if self.comboBox_10.currentText() == "월별매출":
            # 년추출 YEAR(컬럼명)
            # 월추출 MONTH(컬럼명) = "2"
            # 일추출 DAYOFMONTH(컬럼명)
            # DATEDIFF (A,B) 는 A날짜에서 B날짜를 빼는 것
            # CURDATE() 는 오늘 날짜를 추출해줌
            # DATEDIFF(CURDATE(), orderdate) ~일 전
            self.cur.execute("select MONTH(TIME),sum(cost) from order_history "
                             "GROUP BY MONTH(TIME) ORDER BY MONTH(TIME) asc")
            self.result = self.cur.fetchall()
            self.df = pd.DataFrame(data=self.result)
            self.df_list_x = self.df[0].values.tolist()
            self.df_list_y = self.df[1].values.tolist()
            self.de_list_x_ToString = []
            self.de_list_y_ToString = []
            for i in range(len(self.df_list_x)):
                self.de_list_x_ToString.append(str(self.df_list_x[i]))
                self.de_list_y_ToString.append(str(self.df_list_y[i]))
            print(self.de_list_y_ToString)
            self.ax.clear()
            self.ax.bar(self.de_list_x_ToString, self.de_list_y_ToString)
            self.ax.figure.canvas.draw()
        if self.comboBox_10.currentText() == "최근한달매출변화":
            self.cur.execute("select DAYOFMONTH(TIME),SUM(cost) from order_history "
                             "where DATEDIFF(CURDATE(), TIME)<=31 GROUP BY DAYOFMONTH(TIME)")
            self.result = self.cur.fetchall()
            self.df = pd.DataFrame(data=self.result)
            self.df_list_x = self.df[0].values.tolist()
            self.df_list_y = self.df[1].values.tolist()

            self.ax.clear()
            self.ax.plot(self.df_list_x, self.df_list_y)
            self.ax.figure.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()