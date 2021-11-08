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

ip = socket.gethostbyname(socket.gethostname())

import pymysql

# 주문내역넘기기
conn = pymysql.connect(host='localhost',port=3306,user='root'
                       ,password='shs5481',db='branch_main',charset='utf8', autocommit=True)
cur = conn.cursor()
cur.execute('SELECT * FROM order_history')
a = cur.fetchall()
print(a[0])
print(a[0][1])


conn2 = pymysql.connect(host='localhost',port=3306,user='root'
                       ,password='shs5481',db='branch_singa',charset='utf8', autocommit=True)
cur2 = conn2.cursor()
print(len(a))
for i in range(len(a)):
    cur2.execute("INSERT INTO order_history(id,time,menu,quantity,cost,PM,branch) VALUES('{}','{}','{}',{},{},'{}','{}')"
             .format(a[i][0],a[i][1],a[i][2],a[i][3],a[i][4],a[i][5],a[i][6]))

conn3 = pymysql.connect(host='localhost',port=3306,user='root'
                       ,password='shs5481',db='branch_suwan',charset='utf8', autocommit=True)
cur3 = conn3.cursor()
print(len(a))
for i in range(len(a)):
    cur3.execute("INSERT INTO order_history(id,time,menu,quantity,cost,PM,branch) VALUES('{}','{}','{}',{},{},'{}','{}')"
             .format(a[i][0],a[i][1],a[i][2],a[i][3],a[i][4],a[i][5],a[i][6]))

# 아이디넘기기
# conn = pymysql.connect(host='localhost',port=3306,user='root'
#                        ,password='shs5481',db='branch_main',charset='utf8', autocommit=True)
# cur = conn.cursor()
# cur.execute('SELECT * FROM member')
# a = cur.fetchall()
# print(a[0])
# print(a[0][1])
#
#
# conn2 = pymysql.connect(host='localhost',port=3306,user='root'
#                        ,password='shs5481',db='branch_singa',charset='utf8', autocommit=True)
# cur2 = conn2.cursor()
# print(len(a))
# for i in range(len(a)-1):
#     cur2.execute("INSERT INTO member(date,id,pw) VALUES('{}','{}','{}')"
#              .format(a[i][0],a[i][1],a[i][2]))
#
# conn3 = pymysql.connect(host='localhost',port=3306,user='root'
#                        ,password='shs5481',db='branch_suwan',charset='utf8', autocommit=True)
# cur3 = conn3.cursor()
# print(len(a))
# for i in range(len(a)-1):
#     cur3.execute("INSERT INTO member(date,id,pw) VALUES('{}','{}','{}')"
#              .format(a[i][0],a[i][1],a[i][2]))
