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

# ui 창을 화면의 정 가운데에 띄우기 위한 함수 정의
# def center(window):
#     window.setGeometry(
#         QtWidgets.QStyle.alignedRect(
#             QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, window.size(),
#             QtWidgets.qApp.desktop().availableGeometry()))

page1 = uic.loadUiType("../포켓몬/1.ui")[0]
page2 = uic.loadUiType("../포켓몬/2.ui")[0]
page3 = uic.loadUiType("../포켓몬/3.ui")[0]
page4 = uic.loadUiType("../포켓몬/4.ui")[0] #폴더명 경로안에 있을때 자동으로 불러오기

# 내 전력 연산용 변수 모음 클래스
class MyPo:
    a1 = 0  #1피카 2파이 3꼬부 4이상
    a2 = 5  #죽었을때 카운트
    lev = 0  # 초기레벨 0~5 까지
    Hp = 100  # 초기 레벨 0일때 체력
    MaxHP = 100 #최대 체력 값 레벨업시 100씩 증가
    Mp = 10  # 초기 레벨 0일때 마나
    MaxMP = 10 #최대 마나 값 레벨업시 1씩 증가
    attack = 20  # 초기 레벨 0일때 공격력(데미지) 레벨업시 5씩 증가
    exp = 0  # 현재경험치
    Maxexp = 100 #경험치 요구량
    LUexp = [140, 552, 2772, 14256, 10000]  #경험치 요구량 리스트
    LU = 0  #최대 경험치 요구량 리스트 불러오기용 변수

# 적 전력 연산용 변수 모음 클래스
class Enermy:
    lev_e = 0 #적 레벨
    Hp_e = 0 #적 체력
    Mp_e = 10 #적 마나
    attack_e = 0 #적 공격력

    skil_e = ["러스터캐논","마그넷봄","메탈크로우","불릿펀치","아이언테일","돌려차기","마하펀치","바위꺠기","지구던지기","파동탄","폭발펀치",
              "그림자꿰매기","악몽","원한","핥기","더블어택","마구찌르기","막치기","베어가르기","짓밟기","파괴광선","물대포","물의파동","파도타기",
              "하이드로펌프","회오리불꽃","불꽃세례","불꽃펀치","화염방사","냉동빔","오로라빔","얼다바람","10만볼트","번개","볼트태클","솔라빔",
              "덩굴채찍","에너지볼"]

class MainWindow(QMainWindow, page1):  #ui1
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        MyPo.a1 = 0  # 1피카 2파이 3꼬부 4이상
        MyPo.a2 = 5  # 죽었을때 카운트  #카운트 "-1" 누적 방지
        MyPo.lev = 0  # 초기레벨 0~5 까지
        MyPo.Hp = 100  # 초기 레벨 0일때 체력
        MyPo.MaxHP = 100  # 최대 체력 값 레벨업시 100씩 증가
        MyPo.Mp = 10  # 초기 레벨 0일때 마나
        MyPo.MaxMP = 10  # 최대 마나 값 레벨업시 1씩 증가
        MyPo.attack = 20  # 초기 레벨 0일때 공격력(데미지) 레벨업시 5씩 증가
        MyPo.exp = 0  # 경험치
        MyPo.Maxexp = 100
        MyPo.LU = 0


        # # 1page 화면 (수평, 수직) 가운데 정렬
        # lay1 = QtWidgets.QVBoxLayout(self)
        # center(self)
        self.gameStartPushButton.clicked.connect(self.gameStartPushButtonFunction)
        self.helpPushButton.clicked.connect(self.helpPushButtonFunction)

    def gameStartPushButtonFunction(self): #게임시작 누르면 ui2띄우기
        self.select = selectWindow()
        self.select.show()
        self.close()

    # @QtCore.pyqtSlot()      # 메시지창 화면 (수평, 수직) 가운데 정렬
    def helpPushButtonFunction(self): #도움말 누르면 메시지박스 띄우기
        # 도움말 메시지창
        # QMessageBox.information(self,"help","""
        #    < rule >
        #
        #    1. select your game character.\t
        #
        #    2. You will fight with 1 of 10 character.\t
        #
        #    3. If pushing the ATTACK button, you can choice the skill.\t
        #
        #    3. If your HP is '0', GAME OVER.
        #
        #    4. Before HP is '0', using the skill or the item.\t
        #
        #    ** Thank you and enjoy the game **""",QMessageBox.예,QMessageBox.예)
        infoBox = QtWidgets.QMessageBox()
        infoBox.setIcon(QtWidgets.QMessageBox.Information)  # 메시지창 내부 아이콘은 한정돼있는데, Information은 'i'
        infoBox.setWindowTitle("Help")  # 메시지 제목
        infoBox.setText("""
           < rule >

           1. select your game character.\t

           2. You will fight with 1 of 10 character.\t

           3. If pushing the ATTACK button, you can choice the skill.\t

           3. If your HP is '0', GAME OVER.

           4. Before HP is '0', using the skill or the item.\t

           ** Thank you and enjoy the game **""")  # 메시지 내용
        infoBox.setStandardButtons(QMessageBox.Yes)  # 메시지창의 버튼 (|를 이용하여 추가 가능)
        infoBox.setDefaultButton(QMessageBox.Yes)  # 포거크사 지정된 기본 버튼 ㅡ> 기본 버튼 지정 필수
        # wrapper = partial(center, infoBox)  # 화면 정렬 : center 함수 적용
        # QtCore.QTimer.singleShot(0, wrapper)
        infoBox.exec_()

# 2 page
class selectWindow(QMainWindow, page2 ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # # 2page 화면 (수평, 수직) 가운데 정렬
        # # lay2 = QtWidgets.QVBoxLayout(self)
        # center(self)

        self.pikaPushButton.clicked.connect(self.pikaPushButtonFunction) #피카츄 버튼 누를시
        self.piryPushButton.clicked.connect(self.piryPushButtonFunction) #파이리 버튼 누를시
        self.kkobukPushButton.clicked.connect(self.kkobukPushButtonFunction) #꼬부기 버튼 누를시
        self.isangPushButton.clicked.connect(self.isangPushButtonFunction) #이상해씨 버튼 누를시
        self.loadButton.clicked.connect(self.loadButtonFunction)


    def pikaPushButtonFunction(self): #피카츄
        # 내 캐릭터 라벨에 이미지 자동 추가.
        MyPo.a1 = 1  #1번이 피카츄를 뜻함
        self.fightt = fightWindow()  #버튼 누를시 ui3 로 넘어가기
        self.fightt.show()
        self.close()


    def piryPushButtonFunction(self):
        MyPo.a1 = 2
        self.fight = fightWindow()
        self.fight.show()
        self.close()

    def kkobukPushButtonFunction(self):
        MyPo.a1 = 3
        self.fight = fightWindow()
        self.fight.show()
        self.close()

    def isangPushButtonFunction(self):
        MyPo.a1 = 4
        self.fight = fightWindow()
        self.fight.show()
        self.close()

    def loadButtonFunction(self):
        conn = sqlite3.connect("pocket.db")
        cur = conn.cursor()
        btn = pyautogui.prompt(title='불러오기', text='id를 입력하세요.')
        print(btn)
        id_data = btn
        str(id_data)
        print(id_data)
        cur.execute('SELECT * FROM employee_data WHERE id={}'.format(id_data))

        load_data = cur.fetchone()


        conn.close()

        MyPo.a1 = int(load_data[1])
        MyPo.a2 = int(load_data[2])
        MyPo.lev = int(load_data[3])
        MyPo.Hp = int(load_data[4])
        MyPo.MaxHP = int(load_data[5])
        MyPo.Mp = int(load_data[6])
        MyPo.MaxMP = int(load_data[7])
        MyPo.attack = int(load_data[8])
        MyPo.exp = int(load_data[9])
        MyPo.Maxexp = int(load_data[10])
        MyPo.LU = int(load_data[11])

        self.fight = fightWindow()
        self.fight.show()
        self.close()

# 3 page
class fightWindow(QMainWindow, page3 ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # # 3page 화면 (수평, 수직) 가운데 정렬
        # lay3 = QtWidgets.QVBoxLayout(self)
        # center(self)
        Enermy.Mp_e = 10

        self.c = MyPo.a1# 내가 선택한 캐릭터 구분하는 숫자 1=피카츄
        #레벨업 계산
        if MyPo.exp >= MyPo.Maxexp:
            MyPo.lev += 1
            lu = MyPo.LU
            print(MyPo.Maxexp)
            MyPo.Maxexp = int(MyPo.LUexp[lu])
            self.myEXPprogressBar.setMaximum(MyPo.Maxexp)
            print(MyPo.exp)
            MyPo.exp = 0
            self.myEXPprogressBar.setValue(MyPo.exp)
            print(MyPo.Maxexp)
            print(MyPo.exp)

            MyPo.MaxHP += 100
            MyPo.MaxMP += 1
            MyPo.attack += 5
            MyPo.Hp = MyPo.MaxHP
            MyPo.Mp = MyPo.MaxMP
            MyPo.LU += 1

        self.myHPprogressBar.setMaximum(MyPo.MaxHP) #최대 체력바 프로그래스바 설정
        self.myHPprogressBar.setValue(MyPo.Hp)  #현재 체력바 값 설정
        self.myHPprogressBar.setMinimum(0)  #최소 체력바 프로그래스바 설정
        self.myMPprogressBar.setMaximum(MyPo.MaxMP) #마나
        self.myMPprogressBar.setValue(MyPo.Mp)
        self.myMPprogressBar.setMinimum(0)
        self.myEXPprogressBar.setValue(MyPo.exp) #경험치 프로그래스바 값 설정
        self.myEXPprogressBar.setMaximum(MyPo.Maxexp)
        self.enemyMPprogressBar.setMaximum(Enermy.Mp_e)  # 마나
        self.enemyMPprogressBar.setMinimum(0)
        self.enemyMPprogressBar.setValue(Enermy.Mp_e)

        if self.c == 1:  # 선택한 스타팅 포켓몬들 이미지 및 이름 레벨 불러오기
            self.myCharacterLabel.setPixmap(QPixmap("피카츄.png"))
            self.mychar = "피카츄"
            self.myNameLabel.setText("Lv{} {}".format(MyPo.lev, self.mychar))
            self.myskill = ["몸통박치기", "10만볼트", "번개", "볼트태클"]

            self.skill1PushButton.setText(self.myskill[0])
            self.skill2PushButton.setText(self.myskill[1])
            self.skill3PushButton.setText(self.myskill[2])
            self.skill4PushButton.setText(self.myskill[3])

        if self.c == 2:
            self.myCharacterLabel.setPixmap(QPixmap("파이리.png"))
            self.mychar = "파이리"
            self.myNameLabel.setText("Lv{} {}".format(MyPo.lev, self.mychar))
            self.myskill = ["몸통박치기", "할퀴기", "불꽃세례", "화염방사"]

            self.skill1PushButton.setText(self.myskill[0])
            self.skill2PushButton.setText(self.myskill[1])
            self.skill3PushButton.setText(self.myskill[2])
            self.skill4PushButton.setText(self.myskill[3])
        if self.c == 3:
            self.myCharacterLabel.setPixmap(QPixmap("꼬부기.png"))
            self.mychar = "꼬부기"
            self.myNameLabel.setText("Lv{} {}".format(MyPo.lev, self.mychar))
            self.myskill = ["몸통박치기", "물기", "물대포", "하이드로펌프"]

            self.skill1PushButton.setText(self.myskill[0])
            self.skill2PushButton.setText(self.myskill[1])
            self.skill3PushButton.setText(self.myskill[2])
            self.skill4PushButton.setText(self.myskill[3])
        if self.c == 4:
            self.myCharacterLabel.setPixmap(QPixmap("이상해씨.png"))
            self.mychar = "이상해씨"
            self.myNameLabel.setText("Lv{} {}".format(MyPo.lev, self.mychar))
            self.myskill = ["몸통박치기", "잎날가르기", "덩쿨채찍", "솔라빔"]

            self.skill1PushButton.setText(self.myskill[0])
            self.skill2PushButton.setText(self.myskill[1])
            self.skill3PushButton.setText(self.myskill[2])
            self.skill4PushButton.setText(self.myskill[3])

        # 변수를 새롭게 선언해줘야 값을 제대로 넘겨받음
        self.myMp = MyPo.Mp
        self.myHp = MyPo.Hp

        self.rdCharacter = randint(1,10)
        if self.rdCharacter == 1:
            self.enemy = "갸라도스"  # 적1의 이름
            enemypixmap = QPixmap("갸라도스.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  갸라도스".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 갸라도스(이)가 나타났습니다!!----------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바
            # self.enemyMPprogressBar.setMaximum(Enermy.Mp_e)  # 마나
            # self.enemyMPprogressBar.setMinimum(0)
            # self.enemyMPprogressBar.setValue(Enermy.Mp_e)


        elif self.rdCharacter == 2:
            self.enemy = "고라파덕"  # 적1의 이름
            enemypixmap = QPixmap("고라파덕.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  고라파덕".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 고라파덕(이)가 나타났습니다!!----------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바



        elif self.rdCharacter == 3:
            self.enemy = "꼬마돌"  # 적1의 이름
            enemypixmap = QPixmap("꼬마돌.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  꼬마돌".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 꼬마돌(이)가 나타났습니다!!----------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바



        elif self.rdCharacter == 4:
            self.enemy = "독침붕"  # 적1의 이름
            enemypixmap = QPixmap("독침붕.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  독침붕".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 독침붕(이)가 나타났습니다!!----------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바



        elif self.rdCharacter == 5:
            self.enemy = "또도가스"  # 적1의 이름
            enemypixmap = QPixmap("또도가스.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  또도가스".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 또도가스(이)가 나타났습니다!!---------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바



        elif self.rdCharacter == 6:
            self.enemy = "마임맨"  # 적1의 이름
            enemypixmap = QPixmap("마임맨.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  마임맨".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 마임맨(이)가 나타났습니다!!----------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바



        elif self.rdCharacter == 7:
            self.enemy = "망나뇽"  # 적1의 이름
            enemypixmap = QPixmap("망나뇽.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  망나뇽".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 망나뇽(이)가 나타났습니다!!----------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바



        elif self.rdCharacter == 8:
            self.enemy = "버터플"  # 적1의 이름
            enemypixmap = QPixmap("버터플.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  버터플".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 버터풀(이)가 나타났습니다!!----------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바



        elif self.rdCharacter == 9:
            self.enemy = "수륙챙이"  # 적1의 이름
            enemypixmap = QPixmap("수륙챙이.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  수륙챙이".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 수륙챙이(이)가 나타났습니다!!----------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바



        else:
            self.enemy = "식스테일"  # 적1의 이름
            enemypixmap = QPixmap("식스테일.png")
            self.enermyLabel.setPixmap(enemypixmap)
            self.LVe = randint(1, 5)
            self.enemyNameLabel.setText("Lv{}  식스테일".format(self.LVe))
            self.resultTextBrowser.append("-----------야생의 식스테일(이)가 나타났습니다!!----------")

            # 적 스킬 구현중
            self.i = randint(0, 34)
            self.e_skil1 = "몸통박치기"
            self.e_skil2 = Enermy.skil_e[self.i]
            self.e_skil3 = Enermy.skil_e[self.i + 1]
            self.e_skil4 = Enermy.skil_e[self.i + 2]

            if self.LVe == 1:
                Enermy.Hp_e = randint(40, 60)
                Enermy.attack_e = randint(5, 10)

            if self.LVe == 2:
                Enermy.Hp_e = randint(50, 70)
                Enermy.attack_e = randint(6, 11)

            if self.LVe == 3:
                Enermy.Hp_e = randint(60, 80)
                Enermy.attack_e = randint(7, 12)

            if self.LVe == 4:
                Enermy.Hp_e = randint(70, 90)
                Enermy.attack_e = randint(8, 13)

            if self.LVe == 5:
                Enermy.Hp_e = randint(80, 100)
                Enermy.attack_e = randint(9, 14)

            self.enemyHPprogressBar.setMaximum(Enermy.Hp_e)  # 최대 체력바
            self.enemyHPprogressBar.setMinimum(0)
            self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 현재 체력바





        self.attackPushButton.clicked.connect(self.skill_atk) #공격 버튼 누르면 공격다이얼로그 나오게하기
        self.itemPushButton.clicked.connect(self.items_cl) #아이템 버튼 누르면 아이템다이얼로그 나오게하기
        self.nextBattleButton.clicked.connect(self.nextBattleButtonFunction) #리셋 누를시 다른상대와 전투
        self.skill1PushButton.clicked.connect(self.skill1) #기본공격 실행하기
        self.skill2PushButton.clicked.connect(self.skill2)
        self.skill3PushButton.clicked.connect(self.skill3)
        self.skill4PushButton.clicked.connect(self.skill4)

        self.item1PushButton.clicked.connect(self.item1)
        self.item2PushButton.clicked.connect(self.item2)
        self.autoBattleButton.clicked.connect(self.autoBattleButtonFunction)
        self.saveButton.clicked.connect(self.saveButtonFunction)
        self.back.clicked.connect(self.backFunction)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:
            self.skill1()
        elif e.key() == Qt.Key_2:
            self.skill2()
        elif e.key() == Qt.Key_3:
            self.skill3()
        elif e.key() == Qt.Key_4:
            self.skill4()
        elif e.key() == Qt.Key_H:
            self.item1()
        elif e.key() == Qt.Key_M:
            self.item2()

        # elif e.key() == Qt.Key_A:
        #     pyautogui.press('space')
        #




    def enermy_skill(self):
        self.sk_e = randint(1, 4)
        if Enermy.Mp_e >= 2:  # 적의 마나가 2이상일때만 스킬 사용하게 하기
            if self.sk_e == 1:
                eskill = (Enermy.attack_e * 2) - 4  # 적이 스킬을 사용했을경우 내가 입는 피해량을 줄이기위해
                MyPo.Hp -= eskill
                self.myHPprogressBar.setValue(MyPo.Hp)  # 우리팀 체력 프로그래스바 값 변경
                Enermy.Mp_e -= 2
                self.enemyMPprogressBar.setValue(Enermy.Mp_e)
                self.resultTextBrowser.append(
                    "{}(이)가 {}에게 {}기술을 사용하여 {}의 피해를 주었습니다.".format(self.enemy, self.mychar, self.e_skil2, eskill))

            elif self.sk_e == 2:
                eskill = (Enermy.attack_e * 3) - 8
                MyPo.Hp -= eskill
                self.myHPprogressBar.setValue(MyPo.Hp)  # 우리팀 체력 프로그래스바 값 변경
                Enermy.Mp_e -= 4
                self.enemyMPprogressBar.setValue(Enermy.Mp_e)
                self.resultTextBrowser.append(
                    "{}(이)가 {}에게 {}기술을 사용하여 {}의 피해를 주었습니다.".format(self.enemy, self.mychar, self.e_skil3, eskill))

            elif self.sk_e == 3:
                eskill = (Enermy.attack_e * 4) - 12
                MyPo.Hp -= eskill
                self.myHPprogressBar.setValue(MyPo.Hp)  # 우리팀 체력 프로그래스바 값 변경
                Enermy.Mp_e -= 6
                self.enemyMPprogressBar.setValue(Enermy.Mp_e)
                self.resultTextBrowser.append(
                    "{}(이)가 {}에게 {}기술을 사용하여 {}의 피해를 주었습니다.".format(self.enemy, self.mychar, self.e_skil4, eskill))

            else:
                eskill = Enermy.attack_e
                MyPo.Hp -= eskill
                self.myHPprogressBar.setValue(MyPo.Hp)  # 우리팀 체력 프로그래스바 값 변경
                self.enemyMPprogressBar.setValue(Enermy.Mp_e)
                self.resultTextBrowser.append(
                    "{}(이)가 {}에게 {}기술을 사용하여 {}의 피해를 주었습니다.".format(self.enemy, self.mychar, self.e_skil1, eskill))

        else:
            eskill = Enermy.attack_e
            MyPo.Hp -= eskill
            self.myHPprogressBar.setValue(MyPo.Hp)  # 우리팀 체력 프로그래스바 값 변경
            self.resultTextBrowser.append(
                "{}(이)가 {}에게 {}기술을 사용하여 {}의 피해를 주었습니다.".format(self.enemy, self.mychar, self.e_skil1, eskill))

    def items_cl(self):
        self.itemKdialog.show()
        self.itemKdialog.setWindowTitle('items')
        # wrapper = partial(center, self.itemKdialog)
        # QtCore.QTimer.singleShot(0, wrapper)
        self.itemKdialog.exec_()

    def item1(self):
        MyPo.Hp = MyPo.MaxHP
        self.myHPprogressBar.setValue(MyPo.Hp)  # 우리팀 체력 프로그래스바 값 변경

        self.resultTextBrowser.append("내 {}(이)가 아이템1(maxHP)를 썼습니다.".format(self.mychar))  # 피해량 로그 텍스트브라우저에 나오게하기
        self.enermy_skill()

        if Enermy.Hp_e < 0:  # 적 체력 0일시 발생하는것
            self.enemyHPprogressBar.setValue(0)
            MyPo.exp += randint(3, 20)  # 전투 승리시 얻는 경험치
            enermyDown = QMessageBox.information(
                self, '전투결과', "승리했습니다.\n다음 전투를 원하시면 yes 버튼을 눌러주세요",
                QMessageBox.Yes
            )  # 전투 승리시 메시지창뜬후 yes버튼 누르면 다음전투 진행하기
            if enermyDown == QMessageBox.Yes:
                Enermy.Mp_e = 10
                self.nextBattleButton.click()  # 다음전투버튼 자동으로 눌러지게하기
        if MyPo.Hp < 0:  # 우리 캐릭터 체력 0일때 발생
            self.myHPprogressBar.setValue(0)  # 체력 프로그래스바 0으로 보여주기
            self.fight = gameoverWindow()  # ui4 게임오버 로 넘어가기
            self.fight.show()
            self.close()

        self.itemKdialog.close()

    def item2(self):
        MyPo.Mp = MyPo.MaxMP
        self.myMPprogressBar.setValue(MyPo.Mp)  # 우리팀 MP 프로그래스바 값 변경

        self.resultTextBrowser.append("내 {}(이)가 아이템2(maxMP)를 썼습니다.".format(self.mychar))  # 피해량 로그 텍스트브라우저에 나오게하기
        self.enermy_skill()

        if Enermy.Hp_e < 0:  # 적 체력 0일시 발생하는것
            self.enemyHPprogressBar.setValue(0)
            MyPo.exp += randint(3, 20)  # 전투 승리시 얻는 경험치
            enermyDown = QMessageBox.information(
                self, '전투확인', "승리했습니다.\n다음 전투를 원하시면 yes 버튼을 눌러주세요",
                QMessageBox.Yes
            )  # 전투 승리시 메시지창뜬후 yes버튼 누르면 다음전투 진행하기
            if enermyDown == QMessageBox.Yes:
                Enermy.Mp_e = 10
                self.nextBattleButton.click()  # 다음전투버튼 자동으로 눌러지게하기
        if MyPo.Hp < 0:  # 우리 캐릭터 체력 0일때 발생
            self.myHPprogressBar.setValue(0)  # 체력 프로그래스바 0으로 보여주기
            self.fight = gameoverWindow()  # ui4 게임오버 로 넘어가기
            self.fight.show()
            self.close()

        self.itemKdialog.close()

    def skill_atk(self):
        self.skillKdialog.show()
        self.skillKdialog.setWindowTitle('Skills')


        # wrapper = partial(center, self.skillKdialog)
        # QtCore.QTimer.singleShot(0, wrapper)
        if MyPo.Mp < 1: #마나가 1미만일때 스킬2 버튼 비활성화
            self.skill2PushButton.setEnabled(False)
        if MyPo.Mp < 2:
            self.skill3PushButton.setEnabled(False)
        if MyPo.Mp < 3:
            self.skill4PushButton.setEnabled(False)
        if MyPo.Mp >= 1:  # 마나가 1미만일때 스킬2 버튼 비활성화
            self.skill2PushButton.setEnabled(True)
        if MyPo.Mp >= 2:
            self.skill3PushButton.setEnabled(True)
        if MyPo.Mp >= 3:
            self.skill4PushButton.setEnabled(True)

        self.skillKdialog.exec_()

    def skill1(self):
        # 적 공격스킬(랜덤)
        Enermy.Hp_e -= MyPo.attack
        self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 적 체력 프로그래스바 값 변경
        self.resultTextBrowser.append(
            "내 {}(이)가 {} 기술을 사용하여 {}의 피해를 주었습니다.".format(self.mychar, self.myskill[0],
                                                         MyPo.attack))  # 피해량 로그 텍스트브라우저에 나오게하기
        self.enermy_skill()
        if Enermy.Hp_e <= 0:  # 적 체력 0일시 발생하는것
            self.enemyHPprogressBar.setValue(0)
            MyPo.exp += randint(3, 20)
            print(MyPo.exp)# 전투 승리시 얻는 경험치
            Enermy.Mp_e = 10

            # MyPo.Hp += 20  #전투 승리시 자동회복량
            # MyPo.Mp += 2
            enermyDown = QMessageBox.information(
                self, '전투확인', "승리했습니다.\n다음 전투를 원하시면 yes 버튼을 눌러주세요",
                QMessageBox.Yes
            )  # 전투 승리시 메시지창뜬후 yes버튼 누르면 다음전투 진행하기


            if enermyDown == QMessageBox.Yes:
                Enermy.Mp_e = 10
                self.nextBattleButton.click() # 다음전투버튼 자동으로 눌러지게하기
        if MyPo.Hp <= 0:  # 우리 캐릭터 체력 0일때 발생
            self.myHPprogressBar.setValue(0)  # 체력 프로그래스바 0으로 보여주기
            self.fight = gameoverWindow()  # ui4 게임오버 로 넘어가기
            self.fight.show()
            self.close()

        self.skillKdialog.close()

    def skill2(self):
        Enermy.Hp_e -= MyPo.attack * 2
        self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 적 체력 프로그래스바 값 변경
        MyPo.Hp -= Enermy.attack_e
        self.myHPprogressBar.setValue(MyPo.Hp)
        MyPo.Mp -= 1
        self.myMPprogressBar.setValue(MyPo.Mp)

        self.resultTextBrowser.append(
            "내 {}(이)가 {} 기술을 사용하여 {}의 피해를 주었습니다.".format(self.mychar, self.myskill[1], MyPo.attack))
        self.resultTextBrowser.append("내 {}의 MP가 1 줄었습니다.".format(self.mychar, MyPo.Mp))  # 피해량 로그 텍스트브라우저에 나오게하기
        self.enermy_skill()

        if Enermy.Hp_e <= 0:  # 적 체력 0일시 발생하는것
            self.enemyHPprogressBar.setValue(0)
            MyPo.exp += randint(3, 20)  # 전투 승리시 얻는 경험치
            enermyDown = QMessageBox.information(
                self, '전투확인', "승리했습니다.\n다음 전투를 원하시면 yes 버튼을 눌러주세요",
                QMessageBox.Yes
            )  # 전투 승리시 메시지창뜬후 yes버튼 누르면 다음전투 진행하기
            if enermyDown == QMessageBox.Yes:
                self.nextBattleButton.click()  # 다음전투버튼 자동으로 눌러지게하기
        if MyPo.Hp <= 0:  # 우리 캐릭터 체력 0일때 발생
            self.myHPprogressBar.setValue(0)  # 체력 프로그래스바 0으로 보여주기
            self.fight = gameoverWindow()  # ui4 게임오버 로 넘어가기
            self.fight.show()
            self.close()

        self.skillKdialog.close()

    def skill3(self):
        Enermy.Hp_e -= MyPo.attack * 3
        self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 적 체력 프로그래스바 값 변경
        MyPo.Hp -= Enermy.attack_e
        self.myHPprogressBar.setValue(MyPo.Hp)
        MyPo.Mp -= 2
        self.myMPprogressBar.setValue(MyPo.Mp)

        # 우리팀 체력 프로그래스바 값 변경
        self.resultTextBrowser.append(
            "내 {}(이)가 {} 기술을 사용하여 {}의 피해를 주었습니다.".format(self.mychar, self.myskill[2], MyPo.attack))
        self.resultTextBrowser.append("내 {}의 MP가 2 줄었습니다.".format(self.mychar, MyPo.Mp))  # 피해량 로그 텍스트브라우저에 나오게하기
        self.enermy_skill()

        if Enermy.Hp_e <= 0:  # 적 체력 0일시 발생하는것
            self.enemyHPprogressBar.setValue(0)
            MyPo.exp += randint(3, 20)  # 전투 승리시 얻는 경험치
            enermyDown = QMessageBox.information(
                self, '전투확인', "승리했습니다.\n다음 전투를 원하시면 yes 버튼을 눌러주세요",
                QMessageBox.Yes
            )  # 전투 승리시 메시지창뜬후 yes버튼 누르면 다음전투 진행하기
            if enermyDown == QMessageBox.Yes:
                Enermy.Mp_e = 10
                self.nextBattleButton.click()  # 다음전투버튼 자동으로 눌러지게하기
        if MyPo.Hp <= 0:  # 우리 캐릭터 체력 0일때 발생
            self.myHPprogressBar.setValue(0)  # 체력 프로그래스바 0으로 보여주기
            self.fight = gameoverWindow()  # ui4 게임오버 로 넘어가기
            self.fight.show()
            self.close()

        self.skillKdialog.close()

    def skill4(self):
        Enermy.Hp_e -= MyPo.attack * 4
        self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 적 체력 프로그래스바 값 변경
        MyPo.Hp -= Enermy.attack_e
        self.myHPprogressBar.setValue(MyPo.Hp)
        MyPo.Mp -= 3
        self.myMPprogressBar.setValue(MyPo.Mp)

        self.resultTextBrowser.append(
            "내 {}(이)가 {} 기술을 사용하여 {}의 피해를 주었습니다.".format(self.mychar, self.myskill[3], MyPo.attack))
        self.resultTextBrowser.append("내 {}의 MP가 3 줄었습니다.".format(self.mychar, MyPo.Mp))  # 피해량 로그 텍스트브라우저에 나오게하기
        self.enermy_skill()

        if Enermy.Hp_e <= 0:  # 적 체력 0일시 발생하는것
            self.enemyHPprogressBar.setValue(0)
            MyPo.exp += randint(3, 20)  # 전투 승리시 얻는 경험치
            enermyDown = QMessageBox.information(
                self, '전투확인', "승리했습니다.\n다음 전투를 원하시면 yes 버튼을 눌러주세요",
                QMessageBox.Yes
            )  # 전투 승리시 메시지창뜬후 yes버튼 누르면 다음전투 진행하기
            if enermyDown == QMessageBox.Yes:
                Enermy.Mp_e = 10
                self.nextBattleButton.click()  # 다음전투버튼 자동으로 눌러지게하기
        if MyPo.Hp <= 0:  # 우리 캐릭터 체력 0일때 발생
            self.myHPprogressBar.setValue(0)  # 체력 프로그래스바 0으로 보여주기
            self.fight = gameoverWindow()  # ui4 게임오버 로 넘어가기
            self.fight.show()
            self.close()

        self.skillKdialog.close()

    def nextBattleButtonFunction(self): #리셋 누를시 다른상대와 전투
            self.fight = fightWindow()
            self.fight.show()
            self.close()

    def autoBattleButtonFunction(self):
        while MyPo.Hp > 0:
             while Enermy.Hp_e > 0:  #공격돌리기
                Enermy.Hp_e -= MyPo.attack
                self.enemyHPprogressBar.setValue(Enermy.Hp_e)  # 적 체력 프로그래스바 값 변경
                self.resultTextBrowser.append(
                 "내 {}(이)가 {} 기술을 사용하여 {}의 피해를 주었습니다.".format(self.mychar, self.myskill[0],
                                                              MyPo.attack))  # 피해량 로그 텍스트브라우저에 나오게하기
                self.enermy_skill()
                if MyPo.Hp < int((MyPo.MaxHP / 5) * 4):
                    MyPo.Hp += int(MyPo.MaxHP / 5)

             self.enemyHPprogressBar.setValue(0)
             MyPo.exp += randint(3, 20)  # 전투 승리시 얻는 경험치
             self.nextBattleButtonFunction()

             if MyPo.lev == 5 : # 우리 캐릭터 체력 0일때 발생
                 aa = QMessageBox.information(
                     self, '만렙', "축하합니다.\n yes를 누르시면 첫 화면으로 돌아갑니다.",QMessageBox.Yes)
                 if aa == QMessageBox.Yes :
                     self.Main = MainWindow()
                     self.Main.show()
                     self.fight = fightWindow()
                     self.fight.close()
                 break

    def saveButtonFunction(self):
        conn = sqlite3.connect("pocket.db")
        cur = conn.cursor()
        btn = pyautogui.prompt(title='저장하기', text='id를 입력하세요.')
        id = btn
        statedata = (
            ('{}'.format(id), '{}'.format(MyPo.a1), '{}'.format(MyPo.a2), '{}'.format(MyPo.lev),
             '{}'.format(MyPo.Hp), '{}'.format(MyPo.MaxHP), '{}'.format(MyPo.Mp), '{}'.format(MyPo.MaxMP),
             '{}'.format(MyPo.attack), '{}'.format(MyPo.exp), '{}'.format(MyPo.Maxexp), '{}'.format(MyPo.LU))
        )
        print(statedata)
        dbadd = "INSERT INTO pocket_data(id, a1, a2, lev, Hp, MaxHP, Mp, MaxMP, attack, exp, Maxexp, LU)VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
        print("aasda")
        cur.execute(dbadd,statedata)
        print("aaa")

        conn.commit()
        conn.close()

    def backFunction(self):
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        self.close()

class gameoverWindow(QMainWindow, page4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # lay4 = QtWidgets.QVBoxLayout(self)
        # center(self)


        self.a3 = MyPo.a2
        self.restartPushButton.clicked.connect(self.restartPushButtonFunction)
        self.timer = QTimer(self) #게임오버시 다시시작버튼 카운트하기 5 에서 0초
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)
        QTimer.singleShot(5000, self.restartPushButton.click) #5초가 경과대면 자동으로 리셋버튼 눌러서 ui 1로 돌아가기

    def timeout(self):
        self.a3 -= 1
        self.restartlabel.setText("{} 초 후 처음으로 돌아갑니다.".format(self.a3))

    def restartPushButtonFunction(self):
        self.Main = MainWindow()
        self.Main.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()