# 파일 기본
import os
# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir("pythonworkspace")
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())
# os.chdir("E:\githubdesktop-SuperRoketman")
# print(os.getcwd())
# os.chdir("E:\githubdesktop-SuperRoketman\pythonworkspace")
# print(os.getcwd())

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt")
# print(os.path.join(os.getcwd(), "my_file.txt"))

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"E:\githubdesktop-SuperRoketman"))

# 파일 정보 가져오기
# import time
# import datetime

# # 파일의 생성 날짜
# file_path = "e:/githubdesktop-SuperRoketman/pythonworkspace/rpa_basic/2_desktop/11_file_system.py"
# ctime = os.path.getctime(file_path)
# print(ctime)
# # 날짜 정보를 strftime 을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime(file_path)
# print(print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S")))

# # 파일 크기
# size = os.path.getsize(file_path)
# print(size) # 파일 크기 바이트 단위로 가져오기
