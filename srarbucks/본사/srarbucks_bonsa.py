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

page1 = uic.loadUiType("bonsa.ui")[0]

class MainWindow(QMainWindow, page1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.change() # 스택위젯 페이지바뀔 시 다시 디비 커넥트하기 위해 설정

        self.canvas = FigureCanvas(Figure(figsize=(4, 3)))
        self.vbox = QVBoxLayout(self.label)
        self.vbox.addWidget(self.canvas)
        self.ax = self.canvas.figure.subplots()  # xy축 그리기

        sql = "select branch from branch_list"
        self.cur.execute(sql)
        a = self.cur.fetchall()

        self.comboBox.clear()
        for i in range(len(a)):

            self.comboBox.addItem(a[i][0])

        self.lineEdit_pw.setEchoMode(QLineEdit.Password)

        self.pushButton_2.clicked.connect(self.nextpage)  # 로그인
        self.pushButton.clicked.connect(self.inquiry) # 조회1(혜솔)
        self.pushButton_3.clicked.connect(self.entireselect) #조회2(재원)
        self.pushButton_4.clicked.connect(self.delete_bt) # 지점삭제 (영준)
        self.pushButton_5.clicked.connect(self.plus_bt)  # 지점등록 (영준)
        self.pushButton_2.clicked.connect(self.aaa)
        # self.pushButton_2.clicked.connect(self.bbb)
        self.comboBox_5.currentIndexChanged.connect(self.country_changed1)
        self.comboBox_7.currentIndexChanged.connect(self.country_changed2)
        self.comboBox_8.currentIndexChanged.connect(self.country_changed3)


    def aaa(self): #등록된 나라 조회
        sql = "select nation from branch_list GROUP BY nation"
        self.cur.execute(sql)

        a = self.cur.fetchall()  # 등록되어있는 나라 콤보박스로 나타내기
        print(a)
        self.comboBox_5.clear()
        self.comboBox_7.clear()
        for i in range(len(a)):
            self.comboBox_5.addItem(a[i][0])
            self.comboBox_7.addItem(a[i][0])


    def country_changed1(self): #(지점개설)나라 선택하면 그나라에 등록된 도시 조회
        sql = "select country from branch_list where nation like'{}'  GROUP BY country "
        self.cur.execute(sql.format(self.comboBox_5.currentText()))
        aa = self.cur.fetchall()
        print('asdas')
        print(aa)


        self.comboBox_6.clear()

        for i in range(len(aa)):
            self.comboBox_6.addItem(aa[i][0])

    def country_changed2(self): #(그래프)나라 선택하면 그나라에 등록된 도시 조회
        sql = "select country from branch_list where nation like'{}'  GROUP BY country "
        self.cur.execute(sql.format(self.comboBox_7.currentText()))
        aa = self.cur.fetchall()
        print('asdas')
        print(aa)

        self.comboBox_8.clear()

        for i in range(len(aa)):
            self.comboBox_8.addItem(aa[i][0])

    def country_changed3(self): #(그래프)도시 선택하면 그나라에 등록된 지점 조회
        sql = "select branch from branch_list where country like '{}' GROUP BY branch"
        self.cur.execute(sql.format(self.comboBox_8.currentText()))
        aa = self.cur.fetchall()
        print('asdas')
        print(aa)

        self.comboBox.clear()

        for i in range(len(aa)):
            self.comboBox.addItem(aa[i][0])


    def delete_bt(self): # 지점삭제 (영준)
        print('삭제하기')

        self.delete_branch = self.comboBox.currentText()
        print(self.delete_branch)

        delete_message = QMessageBox.information(self, "지점 삭제", "해당지점을 삭제 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        try:
            if delete_message == QMessageBox.Yes:

                self.cur.execute("DELETE FROM branch_list WHERE branch LIKE '{}' ".format(self.delete_branch))
                QtWidgets.QMessageBox.about(self, "지점 삭제", "해당지점 삭제 하셨습니다.")

                sql = "select branch from branch_list"
                self.cur.execute(sql)
                c = self.cur.fetchall()

                self.comboBox.clear()
                for i in range(len(a)):

                    self.comboBox.addItem(c[i][0])


            # else:
            #     QtWidgets.QMessageBox.about(self, "지점 삭제 취소", "해당지점 삭제를 중단하셨습니다.")
        except:
            QtWidgets.QMessageBox.about(self, "오류", "지점 권한이 없습니다.")





    def plus_bt(self):  # 지점등록 (영준)
        self.plus = self.lineEdit.text()
        self.nation_plus = self.comboBox_5.currentText()
        self.country_plus = self.comboBox_6.currentText()
        print(self.nation_plus)
        print(self.country_plus)


        self.cur.execute("select branch from branch_list")
        self.mybranch = self.cur.fetchall()
        print(self.mybranch)
        self.a = 0

        if self.plus == '':
            QtWidgets.QMessageBox.about(self, "지점이름 미지정", "지점의 이름이 지정되지않았습니다.")

        else:
            # QtWidgets.QMessageBox.about(self, "지점 확인 중", "생성되어있는 지점을 확인중입니다.")
            for i in range(len(self.mybranch)):

                if self.plus == self.mybranch[i][0]:
                    print('겹친다')
                    self.a = 1
                    QtWidgets.QMessageBox.about(self, "개설되어있는 지점", "해당지점은 이미 존재합니다.")

                    break
                else:
                    print("안겹침")
                    # QtWidgets.QMessageBox.about(self, "개설되어 있지 않는 지점", "해당지점을 개설 가능합니다.\n잠시만 기다려주세요.")
                    # break

            if self.a == 0:

                self.cur.execute("INSERT INTO branch_list(nation,country,branch) VALUES('{}','{}','{}')".format(self.nation_plus,self.country_plus,self.plus))
                QtWidgets.QMessageBox.about(self, "지점 개설중.", "지점이 개설 되었습니다.")
                sql = "select branch from branch_list where country like '{}' GROUP BY branch"
                self.cur.execute(sql.format(self.comboBox_8.currentText()))

                a = self.cur.fetchall()  # 등록되어있는 지점 콤보박스로 나타내기
                print(a)

                self.comboBox.clear()

                for i in range(len(a)):

                    self.comboBox.addItem(a[i][0])

                self.lineEdit.clear()

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
            id = self.lineEdit_id.text()
            pw = self.lineEdit_pw.text()
            ip = socket.gethostbyname(socket.gethostname())
            conn = pymysql.connect(host='192.168.0.14', port=3306, user=id
                                   , password=pw, db='branch_main', charset='utf8', autocommit=True)
        self.cur = conn.cursor()
        self.setWindowTitle('관리자 프로그램')
        # self.cur.execute('SELECT branch FROM branch_list')  # WHERE id = "{}"'.format(self.label_9.text()))
        # a = self.cur.fetchall()
        # for i in range(len(a)):
        #     self.comboBox.addItem(a[i][0])

        # self.label.setPixmap(QPixmap('rewards-logo.png'))

        # 년추출 YEAR(컬럼명)
        # 월추출 MONTH(컬럼명) = "2"
        # 일추출 DAYOFMONTH(컬럼명)
        # DATEDIFF (A,B) 는 A날짜에서 B날짜를 빼는 것
        # CURDATE() 는 오늘 날짜를 추출해줌
        # DATEDIFF(CURDATE(), orderdate) ~일 전
        # 표 만들기
        self.cur.execute("select branch,time,id,menu,quantity,cost from order_history order by time desc")
        self.result = self.cur.fetchall()
        self.df = pd.DataFrame(data=self.result)
        self.tableWidget.setColumnCount(len(self.df.columns))
        self.tableWidget.setRowCount(len(self.df.index))
        # self.tableWidget.setHorizontalHeaderLabels(df.columns.tolist()) # 열 텍스트 바꾸기
        for i in range(len(self.df.index)):
            for j in range(len(self.df.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))
            # column header 명 설정.
        self.tableWidget.setHorizontalHeaderLabels(['branch', 'time','ID', 'menu', 'quantity', 'cost'])
        self.tableWidget.setSortingEnabled(True) #정렬 가능하게

    def nextpage(self): #로그인
        try:
            id = self.lineEdit_id.text()
            pw = self.lineEdit_pw.text()
            ip = socket.gethostbyname(socket.gethostname())
            conn = pymysql.connect(host='192.168.0.14', port=3306, user=id
                                   , password=pw, db='branch_main', charset='utf8', autocommit=True)
            pyautogui.alert("로그인 성공.")
            myWindow.stackedWidget.setCurrentIndex(self.currentpage - 1)
            self.change()
        except:
            pyautogui.alert("다시 입력해주세요.")

    def inquiry(self): #조회1(혜솔)
        print("id=", id)
        self.branch_name = self.comboBox.currentText()
        print(self.branch_name)
        if self.comboBox_2.currentText() == "vip회원순":
            try:
                self.cur.execute("SELECT id,SUM(cost) FROM order_history WHERE branch LIKE '{}' GROUP BY id ORDER BY SUM(cost) desc".format(self.branch_name))
                result = self.cur.fetchall()
                df = pd.DataFrame(data=result)
                print('1',df)
                self.df_list_x = df[0].values.tolist()
                self.df_list_y = df[1].values.tolist()
            except:
                QtWidgets.QMessageBox.about(self, "신규 지점", "주문내역이 없습니다.")

        if self.comboBox_2.currentText() == "인기메뉴순":
            try:
                self.cur.execute(
                    "SELECT menu,SUM(quantity) FROM order_history WHERE branch LIKE '{}' "
                    "GROUP BY menu ORDER BY SUM(quantity) desc".format(self.branch_name))
                result = self.cur.fetchall()
                df = pd.DataFrame(data=result)
                self.df_list_x = df[0].values.tolist()
                self.df_list_y = df[1].values.tolist()
            except:
                QtWidgets.QMessageBox.about(self, "신규 지점", "주문내역이 없습니다.")
        self.ax.clear()
        self.ax.bar(self.df_list_x, self.df_list_y)
        self.ax.figure.canvas.draw()

    def entireselect(self): #조회2(재원)
        if self.comboBox_3.currentText() == "지점별매출순":
            self.cur.execute("select branch,sum(cost) from order_history GROUP BY branch ORDER BY sum(cost) desc")
            self.result = self.cur.fetchall()
            self.df=pd.DataFrame(data=self.result)
            self.df_list_x = self.df[0].values.tolist()
            self.df_list_y = self.df[1].values.tolist()

            self.ax.clear()
            self.ax.bar(self.df_list_x, self.df_list_y)
            self.ax.figure.canvas.draw()

        if self.comboBox_3.currentText() == "인기메뉴순":
            self.cur.execute("select menu,sum(quantity) from order_history GROUP BY menu ORDER BY sum(quantity) desc")
            self.result = self.cur.fetchall()
            self.df=pd.DataFrame(data=self.result)
            self.df_list_x = self.df[0].values.tolist()
            self.df_list_y = self.df[1].values.tolist()
            self.ax.clear()
            self.ax.bar(self.df_list_x, self.df_list_y)
            self.ax.figure.canvas.draw()

        if self.comboBox_3.currentText() == "월별매출":
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
        if self.comboBox_3.currentText() == "최근한달매출변화":
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