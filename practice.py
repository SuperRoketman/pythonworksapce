# import theater_module
# theater_module.price(3) # 세 명이서 영화보러 갔을 때 가격
# theater_module.price_morning(4) #네 명 조조할인가
# theater_module.price_soldier(5) #다섯 명 군인할인가

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import*
# # from random import*
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7)

# from theater_module import price_soldier as price
# price(5)


# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# import travel.thailand.ThailandPackage # import로 땡겨쓸때는 마지막이 모듈 혹은 패키지.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage #from import 로 하면 클래스 혹은 함수까지 땡기기 가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# from travel import thailand, vietnam
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

#내장함수
# #input
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어던 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "jim"
# print(dir(name))

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서ㅗ 제공하는 기본 기능
# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# # print("오늘 날짜는 ", datetime.date.today())
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)

# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
# import byme
# byme.sige()

# (출력 예제)
# 이 프로그램은 최재윤에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : cook144k@gmail.com

import byme
byme.sign()
