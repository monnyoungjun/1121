
import socket
from PyQt5.QtWidgets import *
import pyautogui
import pymysql
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd  # 데이터 프레임
from PyQt5 import QtWidgets, uic
import sys
from matplotlib.figure import Figure

import datetime, time
now = datetime.datetime.now()
now_year = now.strftime("%Y")
now_month = now.strftime("%M")
now_day = now.strftime("%D")

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

        self.date_changed()

        self.pushButton_2.clicked.connect(self.nextpage)  # 로그인
        self.pushButton.clicked.connect(self.inquiry) # 조회1(혜솔)
        self.pushButton_3.clicked.connect(self.entireselect) #조회2(재원)
        self.pushButton_4.clicked.connect(self.delete_bt) # 지점삭제 (영준)
        self.pushButton_5.clicked.connect(self.plus_bt)  # 지점등록 (영준)
        self.pushButton_2.clicked.connect(self.aaa) #등록된 나라 조회
        self.comboBox_5.currentIndexChanged.connect(self.country_changed1)
        self.comboBox_7.currentIndexChanged.connect(self.country_changed2)
        self.comboBox_8.currentIndexChanged.connect(self.country_changed3)

        # self.pushButton_2.clicked.connect(self.date_changed_MtoD)
        # self.pushButton_2.clicked.connect(self.date_changed_MtoD_2)
        #
        self.comboBox_M1.currentIndexChanged.connect(self.date_changed_MtoD)
        self.comboBox_M2.currentIndexChanged.connect(self.date_changed_MtoD_2)


    def date_changed_MtoD(self):
        self.comboBox_D1.clear()
        if self.comboBox_M1.currentText() == '04' or self.comboBox_M1.currentText()=='06' or self.comboBox_M1.currentText() == '09' or self.comboBox_M1.currentText() == '11':
            for i in range(1,30+1):
                if i < 10:
                    self.comboBox_D1.addItem("0"+str(i))
                else:
                    self.comboBox_D1.addItem(str(i))
        elif self.comboBox_M1.currentText() =='02':
            for i in range(1,28+1):
                if i < 10:
                    self.comboBox_D1.addItem("0" + str(i))
                else:
                    self.comboBox_D1.addItem(str(i))
        else:
            for i in range(1,31+1):
                if i < 10:
                    self.comboBox_D1.addItem("0" + str(i))
                else:
                    self.comboBox_D1.addItem(str(i))
    def date_changed_MtoD_2(self):
        self.comboBox_D2.clear()
        if self.comboBox_M2.currentText() == '04' or self.comboBox_M1.currentText() == '06' or self.comboBox_M1.currentText() == '09' or self.comboBox_M1.currentText() == '11':
            for i in range(1, 30 + 1):
                if i < 10:
                    self.comboBox_D2.addItem("0" + str(i))
                else:
                    self.comboBox_D2.addItem(str(i))
        elif self.comboBox_M2.currentText() == '02':
            for i in range(1, 28 + 1):
                if i < 10:
                    self.comboBox_D2.addItem("0" + str(i))
                else:
                    self.comboBox_D2.addItem(str(i))
        else:
            for i in range(1, 31 + 1):
                if i < 10:
                    self.comboBox_D2.addItem("0" + str(i))
                else:
                    self.comboBox_D2.addItem(str(i))
    def date_changed(self): # 날짜 콤보박스 값 새로 추가
        self.comboBox_Y1.clear()
        self.comboBox_Y2.clear()
        self.comboBox_M1.clear()
        self.comboBox_M2.clear()
        self.comboBox_D1.clear()
        self.comboBox_D2.clear()
        # 날짜 콤보박스 추가
        # 년도 입력
        for i in range(int(now_year),2000,-1):
            self.comboBox_Y1.addItem(str(i))
            self.comboBox_Y2.addItem(str(i))
        # 월 입력
        for i in range(1,12+1):
            if i < 10:
                self.comboBox_M1.addItem("0"+str(i))
                self.comboBox_M2.addItem("0"+str(i))
            else:
                self.comboBox_M1.addItem(str(i))
                self.comboBox_M2.addItem(str(i))
        # 일 입력
        if self.comboBox_M1.currentText() == '04' or self.comboBox_M1.currentText()=='06' or self.comboBox_M1.currentText() == '09' or self.comboBox_M1.currentText() == '11':
            for i in range(1,30+1):
                if i < 10:
                    self.comboBox_D1.addItem("0"+str(i))
                    self.comboBox_D2.addItem("0"+str(i))
                else:
                    self.comboBox_D1.addItem(str(i))
                    self.comboBox_D2.addItem(str(i))
        elif self.comboBox_M1.currentText() =='02':
            for i in range(1,28+1):
                if i < 10:
                    self.comboBox_D1.addItem("0" + str(i))
                    self.comboBox_D2.addItem("0" + str(i))
                else:
                    self.comboBox_D1.addItem(str(i))
                    self.comboBox_D2.addItem(str(i))
        else:
            for i in range(1,31+1):
                if i < 10:
                    self.comboBox_D1.addItem("0" + str(i))
                    self.comboBox_D2.addItem("0" + str(i))
                else:
                    self.comboBox_D1.addItem(str(i))
                    self.comboBox_D2.addItem(str(i))

    def date_changed_2(self): #시작시간 종료시간 재 셋팅
        self.start_time = "{}.{}.{}".format(self.comboBox_Y1.currentText(),self.comboBox_M1.currentText(),self.comboBox_D1.currentText())
        self.end_time = "{}.{}.{}".format(self.comboBox_Y2.currentText(),self.comboBox_M2.currentText(),self.comboBox_D2.currentText())
        print(self.start_time)
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

                sql = "select branch from branch_list where country like '{}' GROUP BY branch"
                self.cur.execute(sql.format(self.comboBox_8.currentText()))
                a = self.cur.fetchall()

                self.comboBox.clear()

                for i in range(len(a)):
                    self.comboBox.addItem(a[i][0])


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
        self.date_changed_2()
        try:
            print("id=", id)
            self.branch_name = self.comboBox.currentText()
            print(self.branch_name)
            if self.comboBox_2.currentText() == "vip회원순":
                print(self.start_time)
                print(self.end_time)
                self.cur.execute("SELECT id,SUM(cost) FROM order_history "
                                 "WHERE branch LIKE '{}' and TIME>='{}' and TIME<='{}' "
                                 "GROUP BY id ORDER BY SUM(cost) desc"
                                 .format(self.branch_name,self.start_time,self.end_time))
                result = self.cur.fetchall()
                df = pd.DataFrame(data=result)
                self.df_list_x = df[0].values.tolist()
                self.df_list_y = df[1].values.tolist()
                self.ax.clear()
                self.ax.bar(self.df_list_x, self.df_list_y)
                self.ax.figure.canvas.draw()
            if self.comboBox_2.currentText() == "인기메뉴순":

                self.cur.execute(
                    "SELECT menu,SUM(quantity) FROM order_history WHERE branch LIKE '{}' and TIME>='{}' and TIME<='{}' "
                    "GROUP BY menu ORDER BY SUM(quantity) desc".format(self.branch_name,self.start_time,self.end_time))
                result = self.cur.fetchall()
                df = pd.DataFrame(data=result)
                self.df_list_x = df[0].values.tolist()
                self.df_list_y = df[1].values.tolist()
                self.ax.clear()
                self.ax.bar(self.df_list_x, self.df_list_y)
                self.ax.figure.canvas.draw()
        except:
            QtWidgets.QMessageBox.about(self, "신규 지점", "주문내역이 없습니다.")



    def entireselect(self): #조회2(재원)
        try:
            self.date_changed_2()
            if self.comboBox_3.currentText() == "지점별매출순":
                self.cur.execute("select branch,sum(cost) from order_history "
                                 "where TIME>='{}' and TIME<='{}' GROUP BY branch "
                                 "ORDER BY sum(cost) desc".format(self.start_time,self.end_time))
                self.result = self.cur.fetchall()
                self.df=pd.DataFrame(data=self.result)
                self.df_list_x = self.df[0].values.tolist()
                print(self.df[0])
                self.df_list_y = self.df[1].values.tolist()

                self.ax.clear()
                self.ax.bar(self.df_list_x, self.df_list_y)
                self.ax.figure.canvas.draw()

            if self.comboBox_3.currentText() == "인기메뉴순":
                self.cur.execute("select menu,sum(quantity) from order_history where TIME>='{}' and TIME<='{}' GROUP BY menu ORDER BY sum(quantity) desc".format(self.start_time,self.end_time))
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
                self.cur.execute("select MONTH(TIME),sum(cost) from order_history where TIME>='{}' and TIME<='{}' GROUP BY MONTH(TIME) ORDER BY MONTH(TIME) asc".format(self.start_time,self.end_time))
                self.result = self.cur.fetchall()
                self.df = pd.DataFrame(data=self.result)
                self.df_list_x = self.df[0].values.tolist()
                self.df_list_y = self.df[1].values.tolist()
                self.de_list_x_ToString = []
                self.de_list_y_ToString = []
                for i in range(len(self.df_list_x)):
                    self.de_list_x_ToString.append(str(self.df_list_x[i]))
                    self.de_list_y_ToString.append(str(self.df_list_y[i]))
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
        except:
            QtWidgets.QMessageBox.about(self, "날짜 지정", "검색할 그래프의 기간을 정해주세요")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()