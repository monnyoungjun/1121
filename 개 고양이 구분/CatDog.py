from PyQt5.QtWidgets import *
import pyautogui
import pymysql
from PyQt5 import QtWidgets, uic
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from keras.models import load_model
import tensorflow.keras
import numpy as np
import cv2
import datetime

conn = pymysql.connect(host='10.10.21.108', user='root', password='1234', db='catdog', charset='utf8')
cur = conn.cursor()

sql = "select * from test"
cur.execute(sql)
aa = cur.fetchall()

print(aa)
conn.commit()
conn.close()

# 지수씨 ip : 10.10.21.108
# 기숙사 wifi ip : 172.16.3.235
# 전산실2(iot?) ip  : 192.168.0.66
# select만 되는 아이디 : aaa / 1234
# 마스터 아이디: root / shs5481

page1 = uic.loadUiType("catdog.ui")[0]


class MainWindow(QMainWindow, page1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sum = random.randint(1, 8)                                   # 사진 이름 숫자
        self.SUM_list = []                             # 사진 중복 체크 리스트

        self.ok_count = 0                              # 정확한 정답의 개수
        self.total_count = 0                           # 검증한 이미지의 총 개수
        self.ok_img = 1                                # OK한 img 이름 숫자

        self.progressBar.setMaximum(0)                 # 현재까지 사진 수
        self.progressBar.setValue(0)                   # 현재까지 ok수
        self.progressBar.setMinimum(0)                 # 최소 숫자 지정

        self.pushButton2.setEnabled(False)             # start 전 ok버튼 막기
        self.pushButton3.setEnabled(False)             # ng버튼 막기

        self.pushButton.clicked.connect(self.start_1)  # 시작
        self.pushButton2.clicked.connect(self.OK)      # 정답
        self.pushButton3.clicked.connect(self.NG)      # 오답
        self.Exit.clicked.connect(self.Exit_1)         # 종료


    def start_1(self):

        try:
            for i in range(len(self.SUM_list)):        # 사진 중복체크
                if len(self.SUM_list) >= 100:
                    exit()

                print(len(self.SUM_list))
                self.sum = random.randint(1, 8)
                while self.sum in self.SUM_list:
                    self.sum = random.randint(1, 8)


            self.SUM_list.append(self.sum)


            print(self.SUM_list)

            np.set_printoptions(suppress=True)


            model = load_model('./my_model2/')

            data = np.ndarray(shape=(1, 128, 128, 3), dtype=np.float32)

            img = cv2.imread("./test/animal ({}).jpg".format(self.sum))

            img = cv2.resize(img, (128, 128))

            image_array = np.asarray(img)

            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            # normalized_image_array = (image_array.astype(np.float32) / 255)

            data[0] = normalized_image_array

            prediction = model.predict(data)


            for i in prediction:
                if i[0] > 0.7:
                    self.AI.setText("개")                                                             # AI라벨에 '개' 입력
                if i[1] > 0.7:
                    self.AI.setText("고양이")                                                          # AI라벨에 '고양이' 입력


            cv2.imwrite("./result/result ({}).jpg".format(self.sum), img)                             # 인식된 사진 저장하기

            label_a = QPixmap("./result/result ({}).jpg".format(self.sum))  # 사진 불러오기

            self.label.setPixmap(label_a)

            self.pushButton.setEnabled(False)                                  # strat시 버튼 막기
            self.pushButton2.setEnabled(True)                                  # ok 버튼 on
            self.pushButton3.setEnabled(True)                                  # ng 버튼 on

        except:
            print("중복")
            self.msgBox = QMessageBox.warning(self, "종료","검증이 종료 되었습니다.",
                                              QMessageBox.Yes, QMessageBox.Yes)
            if self.msgBox == QMessageBox.Yes:
                # DB 저장
                now = datetime.datetime.now()  # 날짜
                nowdate = now.strftime('%Y-%m-%d')
                calculate = (self.ok_count/self.total_count)*100   # 정확도 계산
                print(calculate)
                path2 = "INSERT INTO AIaccuracy VALUES('{}','{}')".format(nowdate,calculate)
                print(path2)
                cur.execute(path2)
                conn.commit()
                conn.close()
                quit()

                # self.label.clear()                                             # 이미지 초기화
                # self.sum = 1                                                   # 사진 이름 숫자
                # self.SUM_list = []                                             # 사진 중복 체크 리스트 초기화
                # self.ok_count = 0                                              # 정확한 정답의 개수 초기화
                # self.total_count = -1                                          # 검증한 이미지의 총 개수 초기화
                # self.ok_img = 1                                                # OK한 img 이름 숫자 초기화
                # self.AI.clear()                                                # AI결과값 지우기
                # self.progressBar.setMaximum(0)                                 # 현재까지 사진 수 리셋
                # self.progressBar.setValue(0)                                   # 현재까지 ok수 리셋
                # self.progressBar.setMinimum(0)                                 # 리셋


    def OK(self):
        self.ok_count += 1
        self.total_count += 1
        self.progressBar.setMaximum(self.total_count)                          # 현재까지 사진 수

        self.progressBar.setValue(self.ok_count)                               # 현재까지 ok수

        # self.start_1()                                                         # start_1함수 실행

        np.set_printoptions(suppress=True)
        img = cv2.imread("./test/animal ({}).jpg".format(self.sum))                                  #
        cv2.imwrite("./OK_img/OK_img ({}).jpg".format(self.sum), img)     # ok된 사진 저장하기기

        self.ok_img += 1                                                                            # 정답 이미지 이름 넘버 +1
                                                                               # 정답 카운트 +1

        now = datetime.datetime.now()                                                               # 날짜
        nowdate = now.strftime('%Y-%m-%d')                                                          # 날짜2

        path = "./OK_img/OK_img ({}).jpg".format(self.sum)                 # 저장할 경로
        ai_text = self.AI.text()                                                                       # AI 분석 값

        self.start_1()  # start_1함수 실행

        sql = "INSERT INTO test VALUES('{}','{}',True,'{}')".format(nowdate,path,ai_text)
        print(sql)
        cur.execute(sql)
        conn.commit()



    def NG(self):
        self.total_count += 1
        self.progressBar.setMaximum(self.total_count)  # 현재까지 사진 수

        self.progressBar.setValue(self.ok_count)  # 현재까지 ok수

        #self.start_1()  # start_1함수 실행

        np.set_printoptions(suppress=True)
        img = cv2.imread("./test/animal ({}).jpg".format(self.sum))  #
        cv2.imwrite("./NG_img/NG_img ({}).jpg".format(self.sum), img)  # ok된 사진 저장하기기

        now = datetime.datetime.now()  # 날짜
        nowdate = now.strftime('%Y-%m-%d')  # 날짜2

        path = "./NG_img/NG_img ({}).jpg".format(self.sum)  # 저장할 경로
        ai_text = self.AI.text()  # AI 분석 값

        self.start_1()  # start_1함수 실행

        sql = "INSERT INTO test VALUES('{}','{}',False,'{}')".format(nowdate, path, ai_text)
        print(sql)
        cur.execute(sql)
        conn.commit()


        # self.total_count += 1
        # self.progressBar.setMaximum(self.total_count)                          # 현재까지 사진 수
        # self.progressBar.setValue(self.ok_count)                               # 현재까지 ok수
        #
        # self.start_1()                                                         # start_1함수 실행


    def Exit_1(self):

        #디비 사진 로그 저장 및 등등 종료 메시지


        quit() # 종료




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()