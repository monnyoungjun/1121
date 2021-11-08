import pymysql
from selenium import webdriver
import threading
import time
import urllib.request
from bs4 import BeautifulSoup
import requests, re,os
import urllib.parse


driver = webdriver.Chrome('chromedriver.exe')             #크롬드라이버 내 크롬 버전에 맞춰서 다운후 .py 프로그램과 같은폴더(경로)에 저장해놓으면 실행
a1 = 2014
url = "https://www.justwatch.com/kr/%EC%98%81%ED%99%94?exclude_genres=rly&exclude_genres=eur&exclude_genres=doc&providers=nfx,prv,wac,wav&release_year_from={}&release_year_until={}".format(a1,a1)
#웹크롤링할 주소
driver.get(url)

SCROLL_PAUSE_TIME = 3
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
SAVE_FLAG = False
def timeout(limit_time): #timeout
    start = time.time()
    while True:
        if time.time() - start > limit_time or SAVE_FLAG:
            raise Exception('timeout. or image saved.')

while True: #검색 결과들을 스크롤해서 미리 로딩해둠.
# Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
# Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".picture-comp__img")
count = 1
i = 0
print("스크롤 완")
print(driver)

ing = []

for image in images:
    SAVE_FLAG = False
    timer = threading.Thread(target=timeout, args=(30,))

    try:
        time.sleep(3)
        timer.start()
        ing.append(driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/div/div/div[2]/div[1]/div/div[{}]/a/div/picture/img'.format(count)).get_attribute("alt"))
        print(ing)
        ing[i] = ing[i].replace(" ", "")
        ing[i] = ing[i].replace(":", "")
        ing[i] = ing[i].replace(".", "")
        ing[i] = ing[i].replace("+", "")
        ing[i] = ing[i].replace("-", "")
        ing[i] = ing[i].replace("*", "")
        ing[i] = ing[i].replace("/", "")
        ing[i] = ing[i].replace("_", "")
        ing[i] = ing[i].replace("?", "")
        ing[i] = ing[i].replace("!", "")
        ing[i] = ing[i].replace("\t", "")
        ing[i] = ing[i].replace("\n", "")
        ing[i] = ing[i].replace("\r", "")
#ing에서 "특정단어" 를 "공백"으로 만듬
        print(ing)
        count += 1
        i += 1
        print(i)
# i = n: 번 성공시 for 그만함
        if i == 50:
            break

    except Exception as e:
        if timer.is_alive():
            timer.join()
        print("실패 할 경우")
        print("********************************")
        pass

count = 1
i = 0

for image in images:
    SAVE_FLAG = False
    timer = threading.Thread(target=timeout, args=(30,))
#타이머 설정
    try:
        time.sleep(2)
        timer.start()
#이미지의 XPath 를 붙여넣기 해준다. >> F12 를 눌러서 페이지 소스의 Element에서 찾아보면됨.
        imgUrl = driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/div/div/div[2]/div[1]/div/div[{}]/a/div/picture/img'.format(count)).get_attribute("src")
        print(imgUrl)
        print("Save images : ./드라마2/{}.jpg".format(count))
        path = "C:/Users/dnjaw/PycharmProjects/pythonProject2/img/" + "{}.jpg".format(ing[i])
        urllib.request.urlretrieve(imgUrl,path) #저장할 이미지의 경로 지정
        SAVE_FLAG = True
        count += 1
        i += 1
        print(count)
        if i == 50:                     #저장할 갯수
            break
        if timer.is_alive():
            timer.join()
    except Exception as e:
        if timer.is_alive():
            timer.join()
        pass

print('driver end. Total images : ', count)
driver.close()

##########################################################################################################
for k in range(len(ing)):

# 영화 이름 받아오기
    try:
        gg = "영화"
        # gggg = "정보"
        ggggg = "{}".format(ing[k])
        ggg = "{} {}".format(gg,ggggg)
        print(ggg)
#입력한 단어를 url로 인코딩하기
        my = urllib.parse.quote(ggg)
        print(my)
#인코딩한 단어를 다음웹사이트 검색어에 입력해서 서치함
        url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={}".format(my)
        print(url)
        source = requests.get(url).text
        soup = BeautifulSoup(source, "html.parser")
        ing3 = []
        a = []
#입력한 영화 정보 리스트화 작업하기
#영화제목
        hotKeys = str(soup.select("#movieTitle > a > b"))
        print(hotKeys)
        a2 = hotKeys.replace("<b>", "")
        a2 = a2.replace("</b>", "")
        a2 = a2.replace("[", "")
        a2 = a2.replace("]", "")
        ing3.append(a2)

#영화 정보들
        hotKeys1 = str(soup.select("#movieEColl > div.coll_cont > div > div.info_movie > div.wrap_cont.type_longtit5 > dl:nth-child(2) > dd.cont"))
        print(hotKeys1)
        print(type(hotKeys1))
        a = hotKeys1.replace('<span class="txt_bar">', "")
        a = a.replace("</span>", "")
        a = a.replace('<dd class="cont">', "")
        a = a.replace('</dd>', "")
        a = a.replace(" ", "")
        a = a.replace("(재)", "")
        a = a.replace("개봉", "")
        a = a.replace("외", "")
        a = a.replace("[", "")
        a = a.replace("]", "")
        a = a.replace(" ", "")
#특정단어들 제거후 split로 특정단어마다 잘라 리스트로 만듬
        a = a.split("|")
        print(a[0])
        print(a[1])
        print(a[2])
        print(a[3])
        print(a[4])
        ing3.append(a[2]) #개봉일
        ing3.append(a[3]) #관람가
        ing3.append(a[0]) #나라
        ing3.append(a[4]) #러닝타임
        ing3.append(a[1]) #장르
        print(ing3)
        print("##############################################################################################")

#평점 가져오기
        gggg = "평점"
        ggg = "{} {} {}".format(gg,ggggg,gggg)
        my = urllib.parse.quote(ggg)
        print(my)
#단어 url로 인코딩한 단어 네이버에 서치후 정보 가져오기
        url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={}".format(my)
        print(url)
        source = requests.get(url).text
        soup = BeautifulSoup(source, "html.parser")
        aa = []

#평점 가져오기
        for i in range(30):
            hotKeys2 = str(soup.select("span.area_star_number"))
            print(hotKeys2)
            print(type(hotKeys2))
            print(len(hotKeys2))

            if len(hotKeys2) != 2:
                aa = hotKeys2.replace('<span class="this_text">',"")
                aa = aa.replace('<span class="area_star_number">', "")
                aa = aa.replace("</span>","")
                aa = aa.replace("[","")
                aa = aa.replace("]","")
                print(aa[0:3])

            else:
                if i == 30:
                    aa = 0
                    print(aa)
                pass
        aa = (float(aa[0:3]))
        print(aa)
        ing3.append(aa)
        ing3.append(0)
        print(ing3)

#마리아 DB에 접속 해서 받은 리스트 값들 마리아 DB에 자동저장하도록함
        conn = pymysql.connect(host='192.168.50.238', user='root', password='wodnjs94', db='movie_kiosk',
                               charset='utf8')  # 접속정보
        cur = conn.cursor()  # 커서생성
        sql = "select mname from movie_all"
        cur.execute(sql)
        resultsd = cur.fetchall()
        print(resultsd)
        ee = 0

        for s in range(len(resultsd)):
            print(ing3[0])
            print(resultsd[s])

#마리아DB에 정보를 가져와 리스트값과 DB값이 같을경우 ee가 1이됨
            if ing3[0] == resultsd[s]:
              ee += 1

#
        if ee != 1:
            sql = "INSERT INTO  movie_all (mname,open,agelimit,country,runningtime,genre1,scores,counts)VALUES('{}','{}','{}','{}','{}','{}',{},{})".format(ing3[0],ing3[1],ing3[2],ing3[3],ing3[4],ing3[5],ing3[6],ing3[7])  # 실행할 sql문
            cur.execute(sql)  # 커서로 sql문 실행
            conn.commit()

        else:
            pass

    except:
        print("실패")
        pass
