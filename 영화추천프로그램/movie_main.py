import sys
import requests
import pymysql
from bs4 import BeautifulSoup
from PyQt5.QtGui import QPixmap , QIcon
from PyQt5.QtCore import Qt , QSize
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import threading
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import dload
import datetime
from bs4 import BeautifulSoup
from pprint import pprint
import requests, re,os
from urllib.request import urlretrieve #추가

#현재시간 구하기
now = datetime.datetime.now()
now.strftime('%Y%m%d%H%M%S')
new_now = now.strftime('%Y%m%d')
print(new_now)
#ui 불러오기
form_class = uic.loadUiType("movie.ui")[0]
form_class2 = uic.loadUiType("movie1.ui")[0]


#다음영화 박스오피스 1~?위 검색
#다음영화 박스오피스 순위 이름 크롤링으로 가져오기
url = "https://movie.daum.net/ranking/boxoffice/weekly?date={}".format(new_now)
print(url)
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")
hotKeys = soup.select("a.link_txt")

ing = []
ing2 = []

index = 0
i = 0
for key in hotKeys:
    index += 1
    print(str(index) + ", " + key.text)                          #저장되는 이름형식
    ing.append(key.text)
    ing2.append(key.text)
    # 이미지 파일에 들어갈 이름 특수문자 , 공백 없애기
    # 이미지 파일에 특수문자 들어갈시 파일손상되서 다운로드된다.
    ing[i] = ing[i].replace(" ","")
    ing[i] = ing[i].replace(":","")
    ing[i] = ing[i].replace(".","")
    ing[i] = ing[i].replace("+", "")
    ing[i] = ing[i].replace("-", "")
    ing[i] = ing[i].replace("*", "")
    ing[i] = ing[i].replace("/", "")
    ing[i] = ing[i].replace("_", "")
    ing[i] = ing[i].replace("?", "")
    ing[i] = ing[i].replace("!", "")
    print(ing)
    i += 1
    if index >= 10:  #갯수
        break        #빠져 나가기

#다음영화 1~10위 스토리 가져오기
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")
hotKeys = soup.select("a.link_story")
story = []
for key in hotKeys:
    index += 1
    print(key.text)                          #저장되는 이름형식
    story.append(key.text)

    i += 1
    if index >= 10:  #갯수
        break

#다음영화 박스오피스 1~10위 이미지 크롤링으로 가져오기
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

data1_list=soup.findAll('div',{'class':'thumb_item'})
print(data1_list)

li_list = []
li_list = data1_list
print(li_list[0])

i = 0

for i in range(10):
    img = li_list[i].find('img')
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(img)
    img_src = img['src']
    print(img_src)
    urlretrieve(img_src , './ranking/{}.jpg'.format(ing[i]))
    urlretrieve(img_src, './images/{}.jpg'.format(ing[i]))

#화면을 띄우는데 사용되는 Class 선언
#####################################메인화면 2 탭 0
class movie(QMainWindow, form_class) :
    def __init__(self, QtGui=None) :
        super().__init__()
        self.setupUi(self)
        self.stacked = QStackedWidget()

        #배경화면 및 박스오피스1위 이미지 삽입
        self.label_9.setPixmap(QPixmap("./ICON/bg1.jpg"))
        self.label_2.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[0])))
        self.logoutbt.setIcon(QIcon("./ICON/Exit.jpg"))

        for i in range(len(ing2)):   #영화 제목 이름 길이가 너무 길면 2줄로 나누어줌
            a1 = ing2[i][0:16]
            a2 = ing2[i][17:36]
            if len(ing2[i]) >= 16:
                ing2[i] = "{}".format(a1) + "\n" + "{}".format(a2)
                print(ing2[i])

        #박스오피스 랭킹 10위 까지 이미지 삽입
        self.ranking_1.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[0])))
        self.rantext_1.setText("{}".format(ing2[0]))
        self.ranking_2.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[1])))
        self.rantext_2.setText("{}".format(ing2[1]))
        self.ranking_3.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[2])))
        self.rantext_3.setText("{}".format(ing2[2]))
        self.ranking_4.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[3])))
        self.rantext_4.setText("{}".format(ing2[3]))
        self.ranking_5.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[4])))
        self.rantext_5.setText("{}".format(ing2[4]))
        self.ranking_6.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[5])))
        self.rantext_6.setText("{}".format(ing2[5]))
        self.ranking_7.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[6])))
        self.rantext_7.setText("{}".format(ing2[6]))
        self.ranking_8.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[7])))
        self.rantext_8.setText("{}".format(ing2[7]))
        self.ranking_9.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[8])))
        self.rantext_9.setText("{}".format(ing2[8]))
        self.ranking_10.setPixmap(QPixmap("./ranking/{}.jpg".format(ing[9])))
        self.rantext_10.setText("{}".format(ing2[9]))


#로그인 화면 버튼 시그널
        self.inputid = self.lineEdit.text()
        self.loginbutton.clicked.connect(self.login)                                   #로그인
        self.exitbutton.clicked.connect(self.exit1)                                    #종료
        self.membership.clicked.connect(self.join_the_membership)                      #회원가입

# 로그인 이후 화면 버튼 시그널 #2번째 화면
        self.gogender.clicked.connect(self.choicegender)                               #추천 받기 버튼
        self.gopage1bt.clicked.connect(self.gopage1)                                   #정보 재수정

#성별 2개 커넥트
        self.boy.pressed.connect(self.boypick2)                                        #남자 선택
        self.boy.clicked.connect(self.choiceage)
        self.boy.clicked.connect(self.boypick)
        self.boy.setIcon(QIcon("./ICON/성별/man.jpg"))
        self.boy.setIconSize(QSize(400, 400))

        self.girl.pressed.connect(self.girlpick2)                                       #여자 선택
        self.girl.clicked.connect(self.choiceage)
        self.girl.clicked.connect(self.girlpick)
        self.girl.setIcon(QIcon("./ICON/성별/woman.jpg"))
        self.girl.setIconSize(QSize(400, 400))


#나이 6개 커넥트
        self.pick10.pressed.connect(self.pick10pick2)
        self.pick10.clicked.connect(self.choicefeeling)
        self.pick10.clicked.connect(self.pick10pick)
        self.pick10.setIcon(QIcon("./ICON/나이/10.jpg"))
        self.pick10.setIconSize(QSize(150, 150))

        self.pick20.pressed.connect(self.pick20pick2)
        self.pick20.clicked.connect(self.choicefeeling)
        self.pick20.clicked.connect(self.pick20pick)
        self.pick20.setIcon(QIcon("./ICON/나이/20.jpg"))
        self.pick20.setIconSize(QSize(150, 150))

        self.pick30.pressed.connect(self.pick30pick2)
        self.pick30.clicked.connect(self.choicefeeling)
        self.pick30.clicked.connect(self.pick30pick)
        self.pick30.setIcon(QIcon("./ICON/나이/30.jpg"))
        self.pick30.setIconSize(QSize(150, 150))

        self.pick40.pressed.connect(self.pick40pick2)
        self.pick40.clicked.connect(self.choicefeeling)
        self.pick40.clicked.connect(self.pick40pick)
        self.pick40.setIcon(QIcon("./ICON/나이/40.jpg"))
        self.pick40.setIconSize(QSize(150, 150))

        self.pick50.pressed.connect(self.pick50pick2)
        self.pick50.clicked.connect(self.choicefeeling)
        self.pick50.clicked.connect(self.pick50pick)
        self.pick50.setIcon(QIcon("./ICON/나이/50.jpg"))
        self.pick50.setIconSize(QSize(150, 150))

        self.pick60.pressed.connect(self.pick60pick2)
        self.pick60.clicked.connect(self.choicefeeling)
        self.pick60.clicked.connect(self.pick60pick)
        self.pick60.setIcon(QIcon("./ICON/나이/60.jpg"))
        self.pick60.setIconSize(QSize(150, 150))


# 감정 상태 6개 커넥트
        self.happy.pressed.connect(self.happypick2)
        self.happy.clicked.connect(self.choiceinterest)
        self.happy.clicked.connect(self.happypick)
        self.happy.setIcon(QIcon("./ICON/감정/행복.png"))
        self.happy.setIconSize(QSize(150, 150))

        self.bored.pressed.connect(self.boredpick2)
        self.bored.clicked.connect(self.choiceinterest)
        self.bored.clicked.connect(self.boredpick)
        self.bored.setIcon(QIcon("./ICON/감정/지루.png"))
        self.bored.setIconSize(QSize(150, 150))

        self.angry.pressed.connect(self.angrypick2)
        self.angry.clicked.connect(self.choiceinterest)
        self.angry.clicked.connect(self.angrypick)
        self.angry.setIcon(QIcon("./ICON/감정/화남.png"))
        self.angry.setIconSize(QSize(150, 150))

        self.surprise.pressed.connect(self.surprisepick2)
        self.surprise.clicked.connect(self.choiceinterest)
        self.surprise.clicked.connect(self.surprisepick)
        self.surprise.setIcon(QIcon("./ICON/감정/놀람.png"))
        self.surprise.setIconSize(QSize(150, 150))

        self.sad.pressed.connect(self.sadpick2)
        self.sad.clicked.connect(self.choiceinterest)
        self.sad.clicked.connect(self.sadpick)
        self.sad.setIcon(QIcon("./ICON/감정/슬픔.png"))
        self.sad.setIconSize(QSize(150, 150))

        self.gloomy.pressed.connect(self.gloomypick2)
        self.gloomy.clicked.connect(self.choiceinterest)
        self.gloomy.clicked.connect(self.gloomypick)
        self.gloomy.setIcon(QIcon("./ICON/감정/우울.png"))
        self.gloomy.setIconSize(QSize(150, 150))


#관심사 9개 커넥트
        self.game.pressed.connect(self.gamepick2)
        self.game.clicked.connect(self.choicegenre)
        self.game.clicked.connect(self.gamepick)
        self.game.setIcon(QIcon("./ICON/관심사/게임.png"))
        self.game.setIconSize(QSize(150, 150))

        self.music.pressed.connect(self.musicpick2)
        self.music.clicked.connect(self.choicegenre)
        self.music.clicked.connect(self.musicpick)
        self.music.setIcon(QIcon("./ICON/관심사/음악.png"))
        self.music.setIconSize(QSize(150, 150))

        self.sports.pressed.connect(self.sportspick2)
        self.sports.clicked.connect(self.choicegenre)
        self.sports.clicked.connect(self.sportspick)
        self.sports.setIcon(QIcon("./ICON/관심사/운동.png"))
        self.sports.setIconSize(QSize(150, 150))

        self.politic.pressed.connect(self.politicpick2)
        self.politic.clicked.connect(self.choicegenre)
        self.politic.clicked.connect(self.politicpick)
        self.politic.setIcon(QIcon("./ICON/관심사/정치.png"))
        self.politic.setIconSize(QSize(150, 150))

        self.love.pressed.connect(self.lovepick2)
        self.love.clicked.connect(self.choicegenre)
        self.love.clicked.connect(self.lovepick)
        self.love.setIcon(QIcon("./ICON/관심사/연애.png"))
        self.love.setIconSize(QSize(150, 150))

        self.work.pressed.connect(self.workpick2)
        self.work.clicked.connect(self.choicegenre)
        self.work.clicked.connect(self.workpick)
        self.work.setIcon(QIcon("./ICON/관심사/일.png"))
        self.work.setIconSize(QSize(150, 150))

        self.travel.pressed.connect(self.travelpick2)
        self.travel.clicked.connect(self.choicegenre)
        self.travel.clicked.connect(self.travelpick)
        self.travel.setIcon(QIcon("./ICON/관심사/여행.png"))
        self.travel.setIconSize(QSize(150, 150))

        self.entertainer.pressed.connect(self.entertainerpick2)
        self.entertainer.clicked.connect(self.choicegenre)
        self.entertainer.clicked.connect(self.entertainerpick)
        self.entertainer.setIcon(QIcon("./ICON/관심사/유명인.png"))
        self.entertainer.setIconSize(QSize(150, 150))

        self.food.pressed.connect(self.foodpick2)
        self.food.clicked.connect(self.choicegenre)
        self.food.clicked.connect(self.foodpick)
        self.food.setIcon(QIcon("./ICON/관심사/음식.png"))
        self.food.setIconSize(QSize(150, 150))


#선호 장르 11개 커넥트
        self.musical.pressed.connect(self.musicalpick2)
        self.musical.clicked.connect(self.musicalpick)
        self.musical.clicked.connect(self.goresult)
        self.musical.setIcon(QIcon("./ICON/장르/뮤지컬.png"))
        self.musical.setIconSize(QSize(150, 150))

        self.thrill.pressed.connect(self.thrillpick2)
        self.thrill.clicked.connect(self.thrillpick)
        self.thrill.clicked.connect(self.goresult)
        self.thrill.setIcon(QIcon("./ICON/장르/스릴.png"))
        self.thrill.setIconSize(QSize(150, 150))

        self.ani.pressed.connect(self.anipick2)
        self.ani.clicked.connect(self.anipick)
        self.ani.clicked.connect(self.goresult)
        self.ani.setIcon(QIcon("./ICON/장르/애니메이션.png"))
        self.ani.setIconSize(QSize(150, 150))

        self.action.pressed.connect(self.actionpick2)
        self.action.clicked.connect(self.actionpick)
        self.action.clicked.connect(self.goresult)
        self.action.setIcon(QIcon("./ICON/장르/액션.png"))
        self.action.setIconSize(QSize(150, 150))

        self.child.pressed.connect(self.childpick2)
        self.child.clicked.connect(self.childpick)
        self.child.clicked.connect(self.goresult)
        self.child.setIcon(QIcon("./ICON/장르/가족.png"))
        self.child.setIconSize(QSize(150, 150))

        self.comedy.pressed.connect(self.comedypick2)
        self.comedy.clicked.connect(self.comedypick)
        self.comedy.clicked.connect(self.goresult)
        self.comedy.setIcon(QIcon("./ICON/장르/코메디.png"))
        self.comedy.setIconSize(QSize(150, 150))

        self.crime.pressed.connect(self.crimepick2)
        self.crime.clicked.connect(self.crimepick)
        self.crime.clicked.connect(self.goresult)
        self.crime.setIcon(QIcon("./ICON/장르/범죄.png"))
        self.crime.setIconSize(QSize(150, 150))

        self.drama.pressed.connect(self.dramapick2)
        self.drama.clicked.connect(self.dramapick)
        self.drama.clicked.connect(self.goresult)
        self.drama.setIcon(QIcon("./ICON/장르/드라마.png"))
        self.drama.setIconSize(QSize(150, 150))

        self.fantasy.pressed.connect(self.fantasypick2)
        self.fantasy.clicked.connect(self.fantasypick)
        self.fantasy.clicked.connect(self.goresult)
        self.fantasy.setIcon(QIcon("./ICON/장르/판타지.png"))
        self.fantasy.setIconSize(QSize(150, 150))

        self.horror.pressed.connect(self.horrorpick2)
        self.horror.clicked.connect(self.horrorpick)
        self.horror.clicked.connect(self.goresult)
        self.horror.setIcon(QIcon("./ICON/장르/공포.png"))
        self.horror.setIconSize(QSize(150, 150))

        self.romance.pressed.connect(self.romancepick2)
        self.romance.clicked.connect(self.romancepick)
        self.romance.clicked.connect(self.goresult)    ##추천
        self.romance.setIcon(QIcon("./ICON/장르/로맨스.png"))
        self.romance.setIconSize(QSize(150, 150))

        self.givethumb.clicked.connect(self.putdbthumb) #추천하기
        self.alreadysaw.clicked.connect(self.putbddata) #본 영화 누르기
        self.logoutbt.clicked.connect(self.exit2)  #끝내기
        self.givethumb_2.clicked.connect(self.goresult)  ##재추천




    def exit2(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.stackedWidget.setCurrentIndex(0)

    def boypick2(self):
        self.boy.setIcon(QIcon("./ICON/성별/man2.jpg"))
        self.boy.setIconSize(QSize(400, 400))

    def girlpick2(self):
        self.girl.setIcon(QIcon("./ICON/성별/woman2.jpg"))
        self.girl.setIconSize(QSize(400, 400))
#나이 눌렀을때
    def pick10pick2(self):
        self.pick10.setIcon(QIcon("./ICON/나이/10-2.jpg"))
        self.pick10.setIconSize(QSize(150, 150))

    def pick20pick2(self):
        self.pick20.setIcon(QIcon("./ICON/나이/20-2.jpg"))
        self.pick20.setIconSize(QSize(150, 150))

    def pick30pick2(self):
        self.pick30.setIcon(QIcon("./ICON/나이/30-2.jpg"))
        self.pick30.setIconSize(QSize(150, 150))

    def pick40pick2(self):
        self.pick40.setIcon(QIcon("./ICON/나이/40-2.jpg"))
        self.pick40.setIconSize(QSize(150, 150))

    def pick50pick2(self):
        self.pick50.setIcon(QIcon("./ICON/나이/50-2.jpg"))
        self.pick50.setIconSize(QSize(150, 150))

    def pick60pick2(self):
        self.pick60.setIcon(QIcon("./ICON/나이/60-2.jpg"))
        self.pick60.setIconSize(QSize(150, 150))
#감정 눌렀을때
    def happypick2(self):
        self.happy.setIcon(QIcon("./ICON/감정/행복-2.jpg"))
        self.happy.setIconSize(QSize(150, 150))

    def boredpick2(self):
        self.bored.setIcon(QIcon("./ICON/감정/지루-2.jpg"))
        self.bored.setIconSize(QSize(150, 150))

    def angrypick2(self):
        self.angry.setIcon(QIcon("./ICON/감정/화남-2.jpg"))
        self.angry.setIconSize(QSize(150, 150))

    def surprisepick2(self):
        self.surprise.setIcon(QIcon("./ICON/감정/놀람-2.jpg"))
        self.surprise.setIconSize(QSize(150, 150))

    def sadpick2(self):
        self.sad.setIcon(QIcon("./ICON/감정/슬픔-2.jpg"))
        self.sad.setIconSize(QSize(150, 150))

    def gloomypick2(self):
        self.gloomy.setIcon(QIcon("./ICON/감정/우울-2.jpg"))
        self.gloomy.setIconSize(QSize(150, 150))
#관심사 눌렀을때
    def gamepick2(self):
        self.game.setIcon(QIcon("./ICON/관심사/게임2.jpg"))
        self.game.setIconSize(QSize(150, 150))

    def musicpick2(self):
        self.music.setIcon(QIcon("./ICON/관심사/음악2.jpg"))
        self.music.setIconSize(QSize(150, 150))

    def sportspick2(self):
        self.sports.setIcon(QIcon("./ICON/관심사/운동2.jpg"))
        self.sports.setIconSize(QSize(150, 150))

    def politicpick2(self):
        self.politic.setIcon(QIcon("./ICON/관심사/정치2.jpg"))
        self.politic.setIconSize(QSize(150, 150))

    def lovepick2(self):
        self.love.setIcon(QIcon("./ICON/관심사/연애2.jpg"))
        self.love.setIconSize(QSize(150, 150))

    def workpick2(self):
        self.work.setIcon(QIcon("./ICON/관심사/일2.jpg"))
        self.work.setIconSize(QSize(150, 150))

    def travelpick2(self):
        self.travel.setIcon(QIcon("./ICON/관심사/여행2.jpg"))
        self.travel.setIconSize(QSize(150, 150))

    def entertainerpick2(self):
        self.entertainer.setIcon(QIcon("./ICON/관심사/유명인2.jpg"))
        self.entertainer.setIconSize(QSize(150, 150))

    def foodpick2(self):
        self.food.setIcon(QIcon("./ICON/관심사/음식2.jpg"))
        self.food.setIconSize(QSize(150, 150))
#장르 눌렀을때
    def musicalpick2(self):
        self.musical.setIcon(QIcon("./ICON/장르/뮤지컬2.jpg"))
        self.musical.setIconSize(QSize(150, 150))

    def thrillpick2(self):
        self.thrill.setIcon(QIcon("./ICON/장르/스릴2.jpg"))
        self.thrill.setIconSize(QSize(150, 150))

    def anipick2(self):
        self.ani.setIcon(QIcon("./ICON/장르/애니메이션2.jpg"))
        self.ani.setIconSize(QSize(150, 150))

    def actionpick2(self):
        self.action.setIcon(QIcon("./ICON/장르/액션2.jpg"))
        self.action.setIconSize(QSize(150, 150))

    def childpick2(self):
        self.child.setIcon(QIcon("./ICON/장르/가족2.jpg"))
        self.child.setIconSize(QSize(150, 150))

    def comedypick2(self):
        self.comedy.setIcon(QIcon("./ICON/장르/코메디2.jpg"))
        self.comedy.setIconSize(QSize(150, 150))

    def crimepick2(self):
        self.crime.setIcon(QIcon("./ICON/장르/범죄2.jpg"))
        self.crime.setIconSize(QSize(150, 150))

    def dramapick2(self):
        self.drama.setIcon(QIcon("./ICON/장르/드라마2.jpg"))
        self.drama.setIconSize(QSize(150, 150))

    def fantasypick2(self):
        self.fantasy.setIcon(QIcon("./ICON/장르/판타지2.jpg"))
        self.fantasy.setIconSize(QSize(150, 150))

    def horrorpick2(self):
        self.horror.setIcon(QIcon("./ICON/장르/공포2.jpg"))
        self.horror.setIconSize(QSize(150, 150))

    def romancepick2(self):
        self.romance.setIcon(QIcon("./ICON/장르/로맨스2.jpg"))
        self.romance.setIconSize(QSize(150, 150))

##############################시작 메인화면
#로그인 관련
#ip
#교실 192.168.0.49
#기숙사 192.168.50.238

    def login(self):
        try:
            self.inputid = self.lineEdit.text()
            self.inputpw = self.lineEdit_2.text()
            self.conn = pymysql.connect(host='192.168.0.49', user='root', password='wodnjs94', db='movie_kiosk', charset='utf8')	# 접속정보
            self.cur = self.conn.cursor()	# 커서생성
            # DB()
            sql = "SELECT id,pw from user where id = '{}' and pw = '{}' ".format(self.inputid,self.inputpw)# 실행할 sql문
            print(sql)
            self.cur.execute(sql)# 커서로 sql문 실행
            results1 = self.cur.fetchall()
            print(results1)
            print(len(results1))

            if len(results1) == 1:
                self.stackedWidget.setCurrentIndex(1)
                self.tabWidget.setCurrentIndex(0)

            else:
                QtWidgets.QMessageBox.information(self, "Login", "아이디와 비밀번호를 다시 확인해주십시오.")
        except:
            QtWidgets.QMessageBox.information(self, "ERROR", "서버에 연결할 수 없습니다.")

#종료하기
    def exit1(self):
        exit()

    def join_the_membership(self):
        self.ui2 = movie2()
        self.ui2.show()


#성별 선택 이동
    def choicegender(self):
        self.tabWidget.setCurrentIndex(1)

#성별 선택
    def boypick(self):
        sql = "UPDATE user SET gender = 'male' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def girlpick(self):
        sql = "UPDATE user SET gender = 'female' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

#나이 선택 이동
    def choiceage(self):
        self.tabWidget.setCurrentIndex(2)
        self.re_icon()

#나이 선택
    def pick10pick(self):
        sql = "UPDATE user SET age = '10' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()


    def pick20pick(self):
        sql = "UPDATE user SET age = '20' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def pick30pick(self):
        sql = "UPDATE user SET age = '30' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def pick40pick(self):
        sql = "UPDATE user SET age = '40' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def pick50pick(self):
        sql = "UPDATE user SET age = '50' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def pick60pick(self):
        sql = "UPDATE user SET age = '60' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

#감정 상태 선택 이동
    def choicefeeling(self):
        self.tabWidget.setCurrentIndex(3)
        self.re_icon()

    #감정 상태 선택
    def happypick(self):
        sql = "UPDATE user SET feeling = 'happy' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def boredpick(self):
        sql = "UPDATE user SET feeling = 'bored' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def angrypick(self):
        sql = "UPDATE user SET feeling = 'angry' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def surprisepick(self):
        sql = "UPDATE user SET feeling = 'surprise' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def sadpick(self):
        sql = "UPDATE user SET feeling = 'sad' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def gloomypick(self):
        sql = "UPDATE user SET feeling = 'gloomy' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

#관심사 선택 이동
    def choiceinterest(self):
        self.tabWidget.setCurrentIndex(4)
        self.re_icon()

    #관심사 선택
    def workpick(self):
        sql = "UPDATE user SET interest = 'work' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def gamepick(self):
        sql = "UPDATE user SET interest = 'game' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def musicpick(self):
        sql = "UPDATE user SET interest = 'music' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def sportspick(self):
        sql = "UPDATE user SET interest = 'sport' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def politicpick(self):
        sql = "UPDATE user SET interest = 'poliitic' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def lovepick(self):
        sql = "UPDATE user SET interest = 'love' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def travelpick(self):
        sql = "UPDATE user SET interest = 'travel' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def entertainerpick(self):
        sql = "UPDATE user SET interest = 'entertainer' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

    def foodpick(self):
        sql = "UPDATE user SET interest = 'food' WHERE id = '{}'".format(self.inputid)  # 실행할 sql문
        print(sql)
        self.cur.execute(sql)  # 커서로 sql문 실행
        self.conn.commit()

#장르 선택 이동
    def choicegenre(self):
        self.tabWidget.setCurrentIndex(5)
        self.re_icon()

    #장르 선택
    def musicalpick(self):
        sql = "UPDATE user SET genre1 = 'musical' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def thrillpick(self):
        sql = "UPDATE user SET genre1 = 'thrill' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def anipick(self):
        sql = "UPDATE user SET genre1 = 'animation' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def actionpick(self):
        sql = "UPDATE user SET genre1 = 'action' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def childpick(self):
        sql = "UPDATE user SET genre1 = 'child' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def comedypick(self):
        sql = "UPDATE user SET genre1 = 'comedy' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def crimepick(self):
        sql = "UPDATE user SET genre1 = 'crime' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def dramapick(self):
        sql = "UPDATE user SET genre1 = 'drama' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def fantasypick(self):
        sql = "UPDATE user SET genre1 = 'fantasy' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def horrorpick(self):
        sql = "UPDATE user SET genre1 = 'horror' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()

    def romancepick(self):
        sql = "UPDATE user SET genre1 = 'romance' WHERE id = '{}'".format(self.inputid)# 실행할 sql문
        print(sql)
        self.cur.execute(sql)# 커서로 sql문 실행
        self.conn.commit()


###############################################마지막 결과 추천 창#################################################

    def goresult(self):
        self.stackedWidget.setCurrentIndex(2)
        self.re_icon()
        sql = "SELECT genre1 FROM user where id ='{}'".format(self.inputid)
        print(sql)
##############################################################로그인한 id의 저장된 취향장르값 불러오기######################3

        self.cur.execute(sql)  # 커서로 sql문 실행
        results1 = self.cur.fetchall()
        print("555555555555555555555555555555555555555555555555555555555555555555555555555555555555555")
        print(results1[0][0])
        results2 = results1[0][0]
        results2 = results2.replace(' ', "")
        print("results2")
        print(results2)
################################################선택된 장르를 한글(컬럼의 값)으로변환###########################################

        if results2 == "musical":
            results2 = "뮤지컬"
            print("1")
        if results2 == "thrill":
            results2 = "스릴러"
            print("2")
        if results2 == "animation":
            results2 = "애니메이션"
            print("3")
        if results2 == "action":
            results2 = "액션 "
            print("4")
        if results2 == "child":  #가족
            results2 = "드라마"
            print("5")
        if results2 == "comedy":
            results2 = "코미디"
            print("6")
        if results2 == "crime":
            results2 = "범죄"
            print("7")
        if results2 == "drama":
            results2 = "드라마"
            print("8")
        if results2 == "fantasy":
            results2 = "판타지/SF"
            print("9")
        if results2 == "horror":
            results2 = "공포"
            print("10")
        if results2 == "romance":
            results2 = "로맨스/멜로"
            print("11")

        print("results2 = ",results2)
######################################변환한 장르 값으로 값은 장르 영화 랜덤검색###########################################

        sqw = "SELECT * FROM movie_all WHERE genre1 LIKE '{}' ORDER BY RAND() LIMIT 1".format(results2)
        self.cur.execute(sqw)
        results3 = self.cur.fetchall()
        print("results3 = ",results3)
        print("results3[0][0] = ",results3[0][0])
        self.movie_title.setText(results3[0][0])
        a = "{}".format(results3[0][0])
        a = a.replace(':', "")
        a = a.replace(' ', "")
        a = a.replace('(', "")
        a = a.replace(')', "")
        a2 = ("영화"+a)
        print("a2 = ",a2)
###########################################################선택된 장르의 랜덤으로 영화1개 출력하기 #########################

        self.movie_main.setPixmap(QPixmap("./images/{}.jpg".format(a)))

        aa = urllib.parse.quote(a2)
        html = requests.get(
            "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={}".format(aa))
        soup = BeautifulSoup(html.text, 'html.parser')
        html.close()

        data1_list = soup.select("#nmovie_img_0 > a > img")
        print("data1_list = ",data1_list)

        img_src = data1_list[0]['src']
        urlretrieve(img_src, './images/' + a + '.jpg')  # 주소, 파일경로+파일명+확장자

        self.movie_main.setPixmap(QPixmap("./images/{}.jpg".format(a)))

        self.movie_nation.setText(results3[0][3])
        self.movie_year.setText(results3[0][1])
        self.movie_age.setText(results3[0][2])
        self.movie_runningtime.setText(results3[0][4])
        self.movie_star.setText("★"+str(results3[0][6])+"점")
        self.movie_star_2.setText(str(results3[0][7]))
################################영화 스토리 크롤링해서 출력하기 ########################################################

        gg = "영화"
        ggggg = "{}".format(a)
        gggg = "정보"
        ggg = "{} {} {}".format(gg, ggggg, gggg)
        print(ggg)
        my = urllib.parse.quote(ggg)
        print(my)
        url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={}".format(my)
        print(url)
        source = requests.get(url).text
        soup = BeautifulSoup(source, "html.parser")

        # 영화줄거리
        print("22")
        ww = 0
        for ww in range(30):
            print(ww)
            story22 = str(soup.select("#main_pack > div.sc_new.cs_common_module.case_empasis.color_{}._au_movie_content_wrap > div.cm_content_wrap > div.cm_content_area._cm_content_area_synopsis > div > div.intro_box._content > p".format(ww)))
            # story22 = str(soup.select("#main_pack > div.sc_new.cs_common_module.case_empasis.color_14._au_movie_content_wrap > div.cm_content_wrap > div.cm_content_area._cm_content_area_synopsis > div > div.intro_box._content > p"))
            print(story22)
            print(len(story22))
            if len(story22) != 2:
                print("aaa")
                story22 = story22.replace('<p class="text _content_text">', "")
                story22 = story22.replace('</p>', "")
                story22 = story22.replace('[', "")
                story22 = story22.replace(']', "")
                story22 = story22.replace('&lt;', "")
                story22 = story22.replace('&gt;;', "")
                print(story22)

                # 영화 제목 이름 길이가 너무 길면 줄 나누어줌
                a1 = story22[0:20]
                a2 = story22[20:40]
                a3 = story22[40:60]
                a4 = story22[60:80]
                a5 = story22[80:100]
                a6 = story22[100:120]
                a7 = story22[120:140]
                a8 = story22[140:160]
                a9 = story22[160:180]
                a10 = story22[180:200]
                a11 = story22[200:220]
                a12 = story22[220:240]
                a13 = story22[240:260]
                a14 = story22[260:280]
                print("여기다..")
                print(a14)
                if len(story22) >= 16:
                    story22 = "{}".format(a1) + "\n" + "{}".format(a2) + "\n" + "{}".format(a3) + "\n" + "{}".format(
                        a4) + "\n" + "{}".format(a5) + "\n" + "{}".format(a6) + "\n" + "{}".format(
                        a7) + "\n" + "{}".format(a8) + "\n" + "{}".format(a9) + "\n" + "{}".format(a10) \
                              + "\n" + "{}".format(a11) + "\n" + "{}".format(a12) + "\n" + "{}".format(
                        a13) + "\n" + "{}".format(a14) + "\n"
                    print(story22)

                self.movie_story.setText(story22)

            else:
                story22 = str(soup.select(
                    "#main_pack > div.sc_new.cs_common_simple._au_movie_content_wrap > div.cm_content_wrap > div > div.cm_info_box > div.detail_info > div.text_expand._ellipsis > span"))
                if len(story22) != 2:
                    print("aaa")
                    story22 = story22.replace('<p class="text _content_text">', "")
                    story22 = story22.replace('</p>', "")
                    story22 = story22.replace('[', "")
                    story22 = story22.replace(']', "")
                    print(story22)

                    # 영화 제목 이름 길이가 너무 길면 줄 나누어줌
                    a1 = story22[0:20]
                    a2 = story22[20:40]
                    a3 = story22[40:60]
                    a4 = story22[60:80]
                    a5 = story22[80:100]
                    a6 = story22[100:120]
                    a7 = story22[120:140]
                    a8 = story22[140:160]
                    a9 = story22[160:180]
                    a10 = story22[180:200]
                    a11 = story22[200:220]
                    a12 = story22[220:240]
                    a13 = story22[240:260]
                    a14 = story22[260:280]
                    print("여기다..")
                    print(a14)
                    if len(story22) >= 16:
                        story22 = "{}".format(a1) + "\n" + "{}".format(a2) + "\n" + "{}".format(
                            a3) + "\n" + "{}".format(
                            a4) + "\n" + "{}".format(a5) + "\n" + "{}".format(a6) + "\n" + "{}".format(
                            a7) + "\n" + "{}".format(a8) + "\n" + "{}".format(a9) + "\n" + "{}".format(a10) \
                                  + "\n" + "{}".format(a11) + "\n" + "{}".format(a12) + "\n" + "{}".format(
                            a13) + "\n" + "{}".format(a14) + "\n"
                        print(story22)





#추천 후 재설정
    def gopage1(self):
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.re_icon()

#icon 리셋
    def re_icon(self):
        self.boy.setIcon(QIcon("./ICON/성별/man.jpg"))
        self.boy.setIconSize(QSize(400, 400))
        self.girl.setIcon(QIcon("./ICON/성별/woman.jpg"))
        self.girl.setIconSize(QSize(400, 400))
        self.pick10.setIcon(QIcon("./ICON/나이/10.jpg"))
        self.pick10.setIconSize(QSize(150, 150))
        self.pick20.setIcon(QIcon("./ICON/나이/20.jpg"))
        self.pick20.setIconSize(QSize(150, 150))
        self.pick30.setIcon(QIcon("./ICON/나이/30.jpg"))
        self.pick30.setIconSize(QSize(150, 150))
        self.pick40.setIcon(QIcon("./ICON/나이/40.jpg"))
        self.pick40.setIconSize(QSize(150, 150))
        self.pick50.setIcon(QIcon("./ICON/나이/50.jpg"))
        self.pick50.setIconSize(QSize(150, 150))
        self.pick60.setIcon(QIcon("./ICON/나이/60.jpg"))
        self.pick60.setIconSize(QSize(150, 150))
        self.happy.setIcon(QIcon("./ICON/감정/행복.png"))
        self.happy.setIconSize(QSize(150, 150))
        self.bored.setIcon(QIcon("./ICON/감정/지루.png"))
        self.bored.setIconSize(QSize(150, 150))
        self.angry.setIcon(QIcon("./ICON/감정/화남.png"))
        self.angry.setIconSize(QSize(150, 150))
        self.surprise.setIcon(QIcon("./ICON/감정/놀람.png"))
        self.surprise.setIconSize(QSize(150, 150))
        self.sad.setIcon(QIcon("./ICON/감정/슬픔.png"))
        self.sad.setIconSize(QSize(150, 150))
        self.gloomy.setIcon(QIcon("./ICON/감정/우울.png"))
        self.gloomy.setIconSize(QSize(150, 150))
        self.game.setIcon(QIcon("./ICON/관심사/게임.png"))
        self.game.setIconSize(QSize(150, 150))
        self.music.setIcon(QIcon("./ICON/관심사/음악.png"))
        self.music.setIconSize(QSize(150, 150))
        self.sports.setIcon(QIcon("./ICON/관심사/운동.png"))
        self.sports.setIconSize(QSize(150, 150))
        self.politic.setIcon(QIcon("./ICON/관심사/정치.png"))
        self.politic.setIconSize(QSize(150, 150))
        self.love.setIcon(QIcon("./ICON/관심사/연애.png"))
        self.love.setIconSize(QSize(150, 150))
        self.work.setIcon(QIcon("./ICON/관심사/일.png"))
        self.work.setIconSize(QSize(150, 150))
        self.travel.setIcon(QIcon("./ICON/관심사/여행.png"))
        self.travel.setIconSize(QSize(150, 150))
        self.entertainer.setIcon(QIcon("./ICON/관심사/유명인.png"))
        self.entertainer.setIconSize(QSize(150, 150))
        self.food.setIcon(QIcon("./ICON/관심사/음식.png"))
        self.food.setIconSize(QSize(150, 150))
        self.musical.pressed.connect(self.musicalpick2)
        self.musical.clicked.connect(self.goresult)
        self.musical.clicked.connect(self.musicalpick)
        self.musical.setIcon(QIcon("./ICON/장르/뮤지컬.png"))
        self.musical.setIconSize(QSize(150, 150))
        self.thrill.setIcon(QIcon("./ICON/장르/스릴.png"))
        self.thrill.setIconSize(QSize(150, 150))
        self.ani.setIcon(QIcon("./ICON/장르/애니메이션.png"))
        self.ani.setIconSize(QSize(150, 150))
        self.action.setIcon(QIcon("./ICON/장르/액션.png"))
        self.action.setIconSize(QSize(150, 150))
        self.child.setIcon(QIcon("./ICON/장르/가족.png"))
        self.child.setIconSize(QSize(150, 150))
        self.comedy.setIcon(QIcon("./ICON/장르/코메디.png"))
        self.comedy.setIconSize(QSize(150, 150))
        self.crime.setIcon(QIcon("./ICON/장르/범죄.png"))
        self.crime.setIconSize(QSize(150, 150))
        self.drama.setIcon(QIcon("./ICON/장르/드라마.png"))
        self.drama.setIconSize(QSize(150, 150))
        self.fantasy.setIcon(QIcon("./ICON/장르/판타지.png"))
        self.fantasy.setIconSize(QSize(150, 150))
        self.horror.setIcon(QIcon("./ICON/장르/공포.png"))
        self.horror.setIconSize(QSize(150, 150))
        self.romance.setIcon(QIcon("./ICON/장르/로맨스.png"))
        self.romance.setIconSize(QSize(150, 150))


#영화 추천
    def putdbthumb(self):
        print(self.movie_title.text())
        try:
            # already 디비 thumbcheck 에 표시 조회 0일시 추천 전이고 1일시 추천
            self.resultname1 = self.movie_title.text()

            self.inputid = self.lineEdit.text()
            sql = "SELECT thumbcheck FROM already WHERE id ='{}' and moviename ='{}' ".format(self.inputid,self.resultname1)
            self.cur.execute(sql)  # 커서로 sql문 실행
            results199 = self.cur.fetchall()
            print("aaaaaaaaaaaaaaaaaaa")
            print(results199)
            print(results199[0])
            print(len(results199))
            # 이미 추천===>메시지 박스만 출력
            try:
                if results199[0] == ('1',):
                    QtWidgets.QMessageBox.information(self, "QMessageBox", "이미 추천하셧습니다.")
                # 미추천 이지만 아이디와 영화제목은 등록되어잇는 경우===>추천수 증가및 추천체크 1로 변경
                elif results199[0] == (None,):
                    sqp = "UPDATE movie_all AS A,already AS B SET A.counts = counts + 1 ,B.thumbcheck = 1 WHERE A.mname ='{}' AND (B.id ='{}'and B.moviename ='{}')"\
                        .format(self.resultname1, self.inputid, self.resultname1)
                    QtWidgets.QMessageBox.information(self, "QMessageBox", "추천이 완료되었습니다.")
                    self.cur.execute(sqp)
                    self.conn.commit()
                # 미추천이고 아이디와 영화 둘다 미등록=====>already 디비에 아이디 영화제목 추천체크 넣기 and 추천수증가
                elif len(results199) == 1:
                    insql = "UPDATE already SET thumbcheck = 1 WHERE id = '{}' AND moviename = '{}')".format(self.inputid,self.resultname1)
                    upsql = "UPDATE movie_all SET counts = counts +1 WHERE mname ='{}' ".format(self.resultname1)
                    self.cur.execute(insql)
                    self.cur.execute(upsql)
                    self.conn.commit()
                    QtWidgets.QMessageBox.information(self, "QMessageBox", "추천이 완료되었습니다.")
            except:
                QtWidgets.QMessageBox.information(self, "오류", "오류코드:E000002")
        except:
            QtWidgets.QMessageBox.information(self, "오류", "오류코드:E000001")

    def putbddata(self):  # 본 영화
        print("sssdad")
        try:
            self.resultname1 = self.movie_title.text()
            self.qwe = "SELECT mark FROM already where id ='{}' and moviename ='{}'".format(self.inputid,
                                                                                            self.resultname1)
            self.cur.execute(self.qwe)
            print(self.qwe)
            result200 = self.cur.fetchall()
            print(result200)
            # print(result200[0])
            # print(result200[0][0])
            if result200 == ():
                print("없는지")
                sqlss = "INSERT INTO already (id,moviename,mark) values('{}','{}',1)".format(self.inputid,
                                                                                             self.resultname1)
                self.cur.execute(sqlss)
                self.conn.commit()
                QtWidgets.QMessageBox.information(self, "QMessageBox", "본 영화 등록이 완료되었습니다.")
            elif result200[0][0] == 1:
                print("ssddff")
                #     print("있는지")
                QtWidgets.QMessageBox.information(self, "오류", "이미 등록하신 영화입니다.")

        except:
            QtWidgets.QMessageBox.information(self, "오류", "오류코드:E000001")

###################################################################################################
##회원가입 다이얼로그 부분

#교실 192.168.0.49
#기숙사 192.168.50.238

class movie2(QDialog, form_class2) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.check_id.clicked.connect(self.check)
        self.membershipjoin.clicked.connect(self.join_membership)
        self.exit2.clicked.connect(self.exit2_1)

    def exit2_1(self):
        self.close()

    def check(self):
        self.new_id2 = self.new_id.text()
        print(self.new_id)
        if len(self.new_id2) > 4:
            #메인 코드
             conn = pymysql.connect(host='192.168.0.49', user='root', password='wodnjs94', db='movie_kiosk', charset='utf8')	# 접속정보
             cur = conn.cursor()	# 커서생성
             sql = "SELECT id from user where id = '{}' ".format(self.new_id2)# 실행할 sql문
             print(sql)
             cur.execute(sql)# 커서로 sql문 실행
             resultsd = cur.fetchall()
             print(resultsd)
             if len(resultsd) == 1:
                QtWidgets.QMessageBox.information(self, "QMessageBox", "이미 존재하는 아이디 입니다.")
             else:
                QtWidgets.QMessageBox.information(self, "QMessageBox", "사용 가능한 아이디 입니다.")
        else:
            QtWidgets.QMessageBox.information(self, "QMessageBox", "아이디를 5자 이상 적어주세요.")



    def join_membership(self):
        self.new_id2 = self.new_id.text()
        self.new_pw2 = self.new_pw.text()
        if len(self.new_id2) > 4 and len(self.new_pw2) !=0:
            conn = pymysql.connect(host='192.168.0.49', user='root', password='wodnjs94', db='movie_kiosk', charset='utf8')	# 접속정보
            cur = conn.cursor()	# 커서생성
            sql = "SELECT id from user where id = '{}' ".format(self.new_id2)	# 실행할 sql문
            print(sql)
            cur.execute(sql)# 커서로 sql문 실행
            resultss = cur.fetchall()
            print(len(resultss))
            if len(resultss) == 1:
                QtWidgets.QMessageBox.information(self, "QMessageBox", "이미 존재하는 아이디 입니다.")
                pass
            else:
                conn = pymysql.connect(host='192.168.0.49', user='root', password='wodnjs94', db='movie_kiosk',
                                       charset='utf8')  # 접속정보
                cur = conn.cursor()  # 커서생성
                sql = "INSERT INTO  user (id,pw)VALUES('{}','{}')".format(self.new_id2,self.new_pw2)  # 실행할 sql문
                print(sql)
                cur.execute(sql)  # 커서로 sql문 실행
                conn.commit()
                QtWidgets.QMessageBox.information(self, "회원가입 완료", "회원가입이 완료되었습니다.")
                self.new_id.clear()
                self.new_pw.clear()
                conn.close()

        else:
            QtWidgets.QMessageBox.information(self, "QMessageBox", "아이디와 비밀번호를 다시 한번 확인해주십시오.")
            self.new_pw.clear()



#실행
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = movie()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

