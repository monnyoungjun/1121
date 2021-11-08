import sys
from PyQt5.QtWidgets import *
#QPushButton=버튼
from PyQt5.QtCore import *
#특정이벤트를 관리
from PyQt5.QtGui import *


class Exam(QMainWindow):

    aa = None



    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.num2 = 0 # 합계
        self.money = 0 # 충전코인
        self.num3 = 0 # 거스름돈
        self.money2 = 0
        self.statusBar()# 위젯에서는 사용안됨,상태표시줄
        self.statusBar().showMessage('안녕하세요 맥도날드 입니다.')# 밑에상태표시줄에 보일 글

        self.setWindowIcon(QIcon("C:\\Users\dnjaw\PycharmProjects\pythonProject/logo.png")) #로고 이미지 넣기


        self.bl = QLabel(self)
        pixmap = QPixmap("C:\\Users\dnjaw\PycharmProjects\pythonProject/logo.png")
        self.bl.setPixmap(QPixmap(pixmap))
        self.bl.resize(140,100)
        self.bl.move(60,10)

        self.bl1 = QLabel('cDonald\'s',self)
        self.bl1.move(170,30)#라벨의 위치
        self.bl1.resize(250,100)#라벨의 크기
        self.bl1.setFont(QFont("나눔손글씨 펜", 35, QFont.Bold))#폰트및 크기


        self.bl2 = QLabel('※코인충전 후 이용해주세요',self)
        self.bl2.move(100,60)#라벨의 위치
        self.bl2.resize(420,150)#라벨의 크기
        self.bl2.setFont(QFont("나눔손글씨 펜", 20))#폰트및 크기

        self.btn = QPushButton('◀충전▶',self)#버튼생성및 버튼안에 들어가는 글자
        self.btn.resize(120,50)#sizeHint:글씨기준으로 크기정하기
        self.btn.setToolTip('<b>충전을 시작 선택')#버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.btn.move(320,180)#위치선택 왼쪽25,위쪽30
        self.btn.setStyleSheet("background-color: #B1FF47;"
                               "border-style:dashed;"
                               "border-width:3px;"
                               "border-color: #67E841")
        self.btn.setFont(QFont("나눔고딕 ExtraBold", 12))#폰트및 크기
        self.btn.clicked.connect(self.button_event)

        self.btn1 = QPushButton('<< 주문하기 >>',self)#버튼생성및 버튼안에 들어가는 글자
        self.btn1.resize(450,60)#sizeHint:글씨기준으로 크기정하기
        self.btn1.setToolTip('<b>주문을 시작 선택')#버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.btn1.move(25,250)#위치선택 왼쪽25,위쪽30
        self.btn1.setStyleSheet("background-color: #B1FF47;"
                                "border-style:dashed;"
                                "border-width:5px;"
                                "border-color: #67E841")
        self.btn1.setFont(QFont("나눔손글씨 펜", 25))#폰트및 크기

        self.bl3 = QLabel('충전된 코인:',self)
        self.bl3.move(40,280)#라벨의 위치
        self.bl3.resize(400,150)#라벨의 크기
        self.bl3.setFont(QFont("나눔손글씨 펜", 20))#폰트및 크기

        self.text1 = QLineEdit(self) #충전금액적는곳
        self.text1.move(50,180)
        self.text1.resize(250,50)
        self.text1.setFont(QFont("나눔손글씨 펜", 20))#폰트및 크기
        self.text1.setStyleSheet("color:blue;"
                               "background-color:#87CEFA;"
                               "border-style:dashed;"
                               "border-width:3px;"
                               "border-color:#1E90FF")

        self.bl4 = QLabel('',self) # 충전된 코인 입력되는 라벨
        self.bl4.move(180,330)#라벨의 위치
        self.bl4.resize(200,50)#라벨의 크기
        self.bl4.setFont(QFont("나눔손글씨 펜", 20))#폰트및 크기


        self.bl5 = QLabel('코인',self)
        self.bl5.move(380,280)#라벨의 위치
        self.bl5.resize(400,150)#라벨의 크기
        self.bl5.setFont(QFont("나눔손글씨 펜", 20))#폰트및 크기

        self.btn1.clicked.connect(self.test)

        self.resize(500,430)#창크기 resize하면 저절로 정중앙에뜸
        self.setWindowTitle('McDonald\'s')

        self.show()

    def test(self):  # 다이얼로그 (누르면 새창) 설정
        self.aa = QDialog()
        self.aa.setWindowTitle(' 주문하기 ')
        self.aa.setWindowModality(Qt.ApplicationModal)
        self.aa.resize(800, 1300)  # 다이얼로그 창 크기

        self.bl4 = QLabel('※메뉴를 선택해 주세요', self.aa)  # 라벨
        self.bl4.move(20, 2)  # 라벨의 위치
        self.bl4.resize(450, 80)  # 라벨의 크기
        self.bl4.setFont(QFont("나눔손글씨 펜", 25))  # 폰트및 크기

        self.bl5 = QLabel('▼버거&세트', self.aa)  # 라벨
        self.bl5.move(20, 20)  # 라벨의 위치
        self.bl5.resize(400, 130)  # 라벨의 크기
        self.bl5.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        # 버거메뉴
        self.qjrj1 = QPushButton('상하이 어니언 버거 / 5200', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.qjrj1.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.qjrj1.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.qjrj1.move(20, 120)  # 위치선택 왼쪽25,위쪽30
        self.qjrj1.setStyleSheet("background-color: #A8ACE8;"
                                 "border-style:dashed;"
                                 "border-width:3px;"
                                 "border-color: #747bdb")
        self.qjrj1.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.qjrj1.clicked.connect(self.qjrjbt1)

        self.qjrj2 = QPushButton('슈니언 버거 / 5200', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.qjrj2.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.qjrj2.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.qjrj2.move(20, 160)  # 위치선택 왼쪽25,위쪽30
        self.qjrj2.setStyleSheet("background-color: #A8ACE8;"
                                 "border-style:dashed;"
                                 "border-width:3px;"
                                 "border-color: #747bdb")
        self.qjrj2.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.qjrj2.clicked.connect(self.qjrjbt2)

        self.qjrj3 = QPushButton('트리플 치즈버거 / 6000', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.qjrj3.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.qjrj3.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.qjrj3.move(20, 200)  # 위치선택 왼쪽25,위쪽30
        self.qjrj3.setStyleSheet("background-color: #A8ACE8;"
                                 "border-style:dashed;"
                                 "border-width:3px;"
                                 "border-color: #747bdb")
        self.qjrj3.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.qjrj3.clicked.connect(self.qjrjbt3)

        self.qjrj4 = QPushButton('맥스파이시 상하이버거 / 5700', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.qjrj4.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.qjrj4.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.qjrj4.move(20, 240)  # 위치선택 왼쪽25,위쪽30
        self.qjrj4.setStyleSheet("background-color: #A8ACE8;"
                                 "border-style:dashed;"
                                 "border-width:3px;"
                                 "border-color: #747bdb")
        self.qjrj4.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.qjrj4.clicked.connect(self.qjrjbt4)

        self.qjrj5 = QPushButton('1955 버거 / 5100', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.qjrj5.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.qjrj5.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.qjrj5.move(20, 280)  # 위치선택 왼쪽25,위쪽30
        self.qjrj5.setStyleSheet("background-color: #A8ACE8;"
                                 "border-style:dashed;"
                                 "border-width:3px;"
                                 "border-color: #747bdb")
        self.qjrj5.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.qjrj5.clicked.connect(self.qjrjbt5)

        self.qjrj6 = QPushButton('빅 맥 / 4800', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.qjrj6.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.qjrj6.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.qjrj6.move(20, 320)  # 위치선택 왼쪽25,위쪽30
        self.qjrj6.setStyleSheet("background-color: #A8ACE8;"
                                 "border-style:dashed;"
                                 "border-width:3px;"
                                 "border-color: #747bdb")
        self.qjrj6.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.qjrj6.clicked.connect(self.qjrjbt6)

        self.bl5 = QLabel('▼사이드', self.aa)  # 라벨
        self.bl5.move(420, 30)  # 라벨의 위치
        self.bl5.resize(420, 130)  # 라벨의 크기
        self.bl5.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기

        self.tkdlem1 = QPushButton('맥윙 1인팩 / 2000', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.tkdlem1.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.tkdlem1.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.tkdlem1.move(420, 120)  # 위치선택 왼쪽25,위쪽30
        self.tkdlem1.setStyleSheet("background-color: #88eed4;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #40c7a5")
        self.tkdlem1.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.tkdlem1.clicked.connect(self.tkdlembt1)

        self.tkdlem2 = QPushButton('후렌치 후라이 / 2300', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.tkdlem2.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.tkdlem2.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.tkdlem2.move(420, 160)  # 위치선택 왼쪽25,위쪽30
        self.tkdlem2.setStyleSheet("background-color: #88eed4;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #40c7a5")
        self.tkdlem2.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.tkdlem2.clicked.connect(self.tkdlembt2)

        self.tkdlem3 = QPushButton('골든 모짜렐라 치즈스틱 / 1500', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.tkdlem3.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.tkdlem3.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.tkdlem3.move(420, 200)  # 위치선택 왼쪽25,위쪽30
        self.tkdlem3.setStyleSheet("background-color: #88eed4;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #40c7a5")
        self.tkdlem3.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기\
        self.tkdlem3.clicked.connect(self.tkdlembt3)

        self.tkdlem4 = QPushButton('상하이 치킨 스낵랩 / 2300', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.tkdlem4.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.tkdlem4.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.tkdlem4.move(420, 240)  # 위치선택 왼쪽25,위쪽3
        self.tkdlem4.setStyleSheet("background-color: #88eed4;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #40c7a5")  # 0
        self.tkdlem4.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.tkdlem4.clicked.connect(self.tkdlembt4)

        self.tkdlem5 = QPushButton('해쉬 브라운 / 2000', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.tkdlem5.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.tkdlem5.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.tkdlem5.move(420, 280)  # 위치선택 왼쪽25,위쪽30
        self.tkdlem5.setStyleSheet("background-color: #88eed4;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #40c7a5")
        self.tkdlem5.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.tkdlem5.clicked.connect(self.tkdlembt5)

        self.tkdlem6 = QPushButton('웨지 후라이 / 2300', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.tkdlem6.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.tkdlem6.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.tkdlem6.move(420, 320)  # 위치선택 왼쪽25,위쪽30
        self.tkdlem6.setStyleSheet("background-color: #88eed4;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #40c7a5")
        self.tkdlem6.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.tkdlem6.clicked.connect(self.tkdlembt6)

        self.bl5 = QLabel('▼디저트', self.aa)  # 라벨
        self.bl5.move(420, 320)  # 라벨의 위치
        self.bl5.resize(400, 130)  # 라벨의 크기
        self.bl5.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기

        self.elwjxm1 = QPushButton('오레오 아포가토 / 2000', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.elwjxm1.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.elwjxm1.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.elwjxm1.move(420, 410)  # 위치선택 왼쪽25,위쪽30
        self.elwjxm1.setStyleSheet("background-color: #cbf157;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #67e841")
        self.elwjxm1.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.elwjxm1.clicked.connect(self.elwjxmbt1)

        self.elwjxm2 = QPushButton('베리스트로베리 맥플러리 / 2300', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.elwjxm2.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.elwjxm2.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.elwjxm2.move(420, 450)  # 위치선택 왼쪽25,위쪽30
        self.elwjxm2.setStyleSheet("background-color: #cbf157;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #67e841")
        self.elwjxm2.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.elwjxm2.clicked.connect(self.elwjxmbt2)

        self.elwjxm3 = QPushButton('오레오 맥플러리 / 2300', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.elwjxm3.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.elwjxm3.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.elwjxm3.move(420, 490)  # 위치선택 왼쪽25,위쪽30
        self.elwjxm3.setStyleSheet("background-color: #cbf157;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #67e841")
        self.elwjxm3.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.elwjxm3.clicked.connect(self.elwjxmbt3)

        self.elwjxm4 = QPushButton('딸기 오레오 맥플러리 / 2300', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.elwjxm4.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.elwjxm4.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.elwjxm4.move(420, 530)  # 위치선택 왼쪽25,위쪽30
        self.elwjxm4.setStyleSheet("background-color: #cbf157;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #67e841")
        self.elwjxm4.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.elwjxm4.clicked.connect(self.elwjxmbt4)

        self.elwjxm5 = QPushButton('초코 오레오 맥플러리 / 2300', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.elwjxm5.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.elwjxm5.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.elwjxm5.move(420, 570)  # 위치선택 왼쪽25,위쪽30
        self.elwjxm5.setStyleSheet("background-color: #cbf157;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #67e841")
        self.elwjxm5.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.elwjxm5.clicked.connect(self.elwjxmbt5)

        self.elwjxm6 = QPushButton('스트로베리콘 / 1000', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.elwjxm6.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.elwjxm6.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.elwjxm6.move(420, 610)  # 위치선택 왼쪽25,위쪽30
        self.elwjxm6.setStyleSheet("background-color: #cbf157;"
                                   "border-style:dashed;"
                                   "border-width:3px;"
                                   "border-color: #67e841")
        self.elwjxm6.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.elwjxm6.clicked.connect(self.elwjxmbt6)

        self.bl5 = QLabel('▼음료', self.aa)  # 라벨
        self.bl5.move(20, 320)  # 라벨의 위치
        self.bl5.resize(400, 130)  # 라벨의 크기
        self.bl5.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기

        self.dmafy1 = QPushButton('초코 쉐이크 / 2000', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.dmafy1.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.dmafy1.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.dmafy1.move(20, 410)  # 위치선택 왼쪽25,위쪽30
        self.dmafy1.setStyleSheet("background-color: #9edbf0;"
                                  "border-style:dashed;"
                                  "border-width:3px;"
                                  "border-color: #1daddd")
        self.dmafy1.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.dmafy1.clicked.connect(self.dmafybt1)

        self.dmafy2 = QPushButton('딸기 쉐이크 / 2000', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.dmafy2.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.dmafy2.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.dmafy2.move(20, 450)  # 위치선택 왼쪽25,위쪽30
        self.dmafy2.setStyleSheet("background-color: #9edbf0;"
                                  "border-style:dashed;"
                                  "border-width:3px;"
                                  "border-color: #1daddd")
        self.dmafy2.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.dmafy2.clicked.connect(self.dmafybt2)

        self.dmafy3 = QPushButton('바닐라 쉐이크 / 1800', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.dmafy3.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.dmafy3.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.dmafy3.move(20, 490)  # 위치선택 왼쪽25,위쪽30
        self.dmafy3.setStyleSheet("background-color: #9edbf0;"
                                  "border-style:dashed;"
                                  "border-width:3px;"
                                  "border-color: #1daddd")
        self.dmafy3.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.dmafy3.clicked.connect(self.dmafybt3)

        self.dmafy4 = QPushButton('오렌지 주스 / 1500', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.dmafy4.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.dmafy4.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.dmafy4.move(20, 530)  # 위치선택 왼쪽25,위쪽30
        self.dmafy4.setStyleSheet("background-color: #9edbf0;"
                                  "border-style:dashed;"
                                  "border-width:3px;"
                                  "border-color: #1daddd")
        self.dmafy4.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.dmafy4.clicked.connect(self.dmafybt4)

        self.dmafy5 = QPushButton('코카-콜라 / 1500', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.dmafy5.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.dmafy5.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.dmafy5.move(20, 570)  # 위치선택 왼쪽25,위쪽30
        self.dmafy5.setStyleSheet("background-color: #9edbf0;"
                                  "border-style:dashed;"
                                  "border-width:3px;"
                                  "border-color: #1daddd")
        self.dmafy5.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.dmafy5.clicked.connect(self.dmafybt5)

        self.dmafy6 = QPushButton('코카-콜라 제로 / 1500', self.aa)  # 버튼생성및 버튼안에 들어가는 글자
        self.dmafy6.resize(360, 30)  # sizeHint:글씨기준으로 크기정하기
        self.dmafy6.setToolTip('<b>클릭시 해당메뉴 선택')  # 버튼에 마우스를 올렸을떄 나오는 힌트작성,<b>굵은글씨
        self.dmafy6.move(20, 610)  # 위치선택 왼쪽25,위쪽30
        self.dmafy6.setStyleSheet("background-color: #9edbf0;"
                                  "border-style:dashed;"
                                  "border-width:3px;"
                                  "border-color: #1daddd")
        self.dmafy6.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.dmafy6.clicked.connect(self.dmafybt6)

        self.text2 = QTextBrowser(self.aa)
        self.text2.move(20, 680)
        self.text2.resize(360, 250)

        self.wldnrl = QPushButton('다시 주문하기', self.aa)
        self.wldnrl.resize(360, 30)
        self.wldnrl.move(420, 680)
        self.wldnrl.setStyleSheet("border-style:dashed;"
                                  "border-width:4px;"
                                  "border-color:#000000")
        self.wldnrl.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.wldnrl.clicked.connect(self.wldnrlbt)

        self.wnansgkrl = QPushButton('주문 결정', self.aa)
        self.wnansgkrl.resize(360, 30)
        self.wnansgkrl.move(420, 720)
        self.wnansgkrl.setStyleSheet("border-style:dashed;"
                                     "border-width:4px;"
                                     "border-color:#000000")
        self.wnansgkrl.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.wnansgkrl.clicked.connect(self.wnansrufwjd)

        self.ehfdkrkrl = QPushButton('돌아가기', self.aa)
        self.ehfdkrkrl.resize(360, 30)
        self.ehfdkrkrl.move(420, 760)
        self.ehfdkrkrl.setStyleSheet("border-style:dashed;"
                                     "border-width:4px;"
                                     "border-color:#000000")
        self.ehfdkrkrl.setFont(QFont("나눔손글씨 펜", 15))  # 폰트및 크기
        self.ehfdkrkrl.clicked.connect(self.ehfdkrkrlbt)

        self.rufwp = QTextBrowser(self.aa)
        self.rufwp.move(420, 800)
        self.rufwp.resize(360, 130)



        self.aa.show()

    def ehfdkrkrlbt(self):
         self.aa.close()

    def button_event(self):
        text = self.text1.text()
        self.money = text
        self.bl4.setText(text)
        print(self.money)


    def wldnrlbt(self):
        self.text2.clear()
        self.num2 = 0
        self.money = self.num3

    def qjrjbt1(self):
        line_text = self.qjrj1.text()
        self.text2.append(line_text)
        self.num2 += 5200

    def qjrjbt2(self):
        line_text = self.qjrj2.text()
        self.text2.append(line_text)
        self.num2 += 5200

    def qjrjbt3(self):
        line_text = self.qjrj3.text()
        self.text2.append(line_text)
        self.num2 += 6000

    def qjrjbt4(self):
        line_text = self.qjrj4.text()
        self.text2.append(line_text)
        self.num2 += 5700

    def qjrjbt5(self):
        line_text = self.qjrj5.text()
        self.text2.append(line_text)
        self.num2 += 5100

    def qjrjbt6(self):
        line_text = self.qjrj6.text()
        self.text2.append(line_text)
        self.num2 += 4800


    def tkdlembt1(self):
        line_text = self.tkdlem1.text()
        self.text2.append(line_text)
        self.num2 += 2000

    def tkdlembt2(self):
        line_text = self.tkdlem2.text()
        self.text2.append(line_text)
        self.num2 += 2300

    def tkdlembt3(self):
        line_text = self.tkdlem3.text()
        self.text2.append(line_text)
        self.num2 += 1500

    def tkdlembt4(self):
        line_text = self.tkdlem4.text()
        self.text2.append(line_text)
        self.num2 += 2300

    def tkdlembt5(self):
        line_text = self.tkdlem5.text()
        self.text2.append(line_text)
        self.num2 += 2000

    def tkdlembt6(self):
        line_text = self.tkdlem6.text()
        self.text2.append(line_text)
        self.num2 += 2300


    def elwjxmbt1(self):
        line_text = self.elwjxm1.text()
        self.text2.append(line_text)
        self.num2 += 2000

    def elwjxmbt2(self):
        line_text = self.elwjxm2.text()
        self.text2.append(line_text)
        self.num2 += 2300

    def elwjxmbt3(self):
        line_text = self.elwjxm3.text()
        self.text2.append(line_text)
        self.num2 += 2300

    def elwjxmbt4(self):
        line_text = self.elwjxm4.text()
        self.text2.append(line_text)
        self.num2 += 2300

    def elwjxmbt5(self):
        line_text = self.elwjxm5.text()
        self.text2.append(line_text)
        self.num2 += 2300

    def elwjxmbt6(self):
        line_text = self.elwjxm6.text()
        self.text2.append(line_text)
        self.num2 += 1000

    def dmafybt1(self):
        line_text = self.dmafy1.text()
        self.text2.append(line_text)
        self.num2 += 2000

    def dmafybt2(self):
        line_text = self.dmafy2.text()
        self.text2.append(line_text)
        self.num2 += 2000

    def dmafybt3(self):
        line_text = self.dmafy3.text()
        self.text2.append(line_text)
        self.num2 += 1800

    def dmafybt4(self):
        line_text = self.dmafy4.text()
        self.text2.append(line_text)
        self.num2 += 1500

    def dmafybt5(self):
        line_text = self.dmafy5.text()
        self.text2.append(line_text)
        self.num2 += 1500

    def dmafybt6(self):
        line_text = self.dmafy6.text()
        self.text2.append(line_text)
        self.num2 += 1500

    def wnansrufwjd(self):
        if int(self.money) >= int(self.num2):
            self.num3 = int(self.money) - int(self.num2)
            self.rufwp.append(('주문이 완료되었습니다.\n남은코인은 {}코인 입니다'.format(int(self.money) - int(self.num2))))
        else:
            self.rufwp.append(('코인이 부족합니다.\n다시 확인후 주문해주세요\n현재코인 {}코인'.format(self.num3)))




    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료확인" , "종료하시겠습니까?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()#이벤트발생 승인
        else:
            QCloseEvent.ignore()#승인불가




app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
