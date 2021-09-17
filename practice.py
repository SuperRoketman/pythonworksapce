# print("Python", "Java", sep = ",", end = "?")
# print("무엇이 더 재미있을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

#시험성적
# scores = {"math":0, "Eng":50, "coding":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8
# ), str(score).rjust(4), sep=":")

#은행 대기순번표
#001 002 003 004
# for num in range(1,21):
#     print("wating : " + str(num).zfill(3))

# answer = input("enter any value : ")
# print(type(answer))
# print("the value entered is " + answer + ".")
# 입력값은 항상 문자열.

# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈 칸을 _로 채움.
# print("{0:_<10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리 마다 콤마를 찍어주기
# print("{0:+,}".format(100000000000))
# # 3자리 마다 콤마를 찍어주기, 부호 붙이고, 자릿수 확보
# # 돈이 많으면 행복하니 빈 자리는 ^로 채워주기
# print("{0:^<+30,}".format(1000000 ))
# # 소숫점 출력
# print("{0:f}".format(5/3))
# # 소숫 점을 특정 자리수 까지만 표시(소숫점 3째자리에서 반올림)
# print("{0:.2f}".format(5/3))


# score_file = open("score.txt", "w", encoding="utf8")
# print("math : 0", file=score_file)
# print("Eng : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("science : 80")
# score_file.write("\ncoding : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"name":"PMS", "age":30, "hobby":["Fb","Golf", "Coding"]}
# print(profile)
# pickle.dump(profile, profile_file) #프로필에 있는 정보를 파일에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

#  - X 주차 주간 보고 -
#  부서 : 
#  이름 : 
#  업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.


#나

# for i in range(1,51):
#     report_file = open("{0}주차.txt".format(i), "w", encoding="utf8")
#     print(""" - {0}주차 주간 보고 - 
#  부서 : 
#  이름 : 
#  업무 요약 : """.format(i), file = report_file)
#     report_file.close()

# for i in range(1, 51):
#     with open("{0}주차.txt".format(i), "w", encoding="utf8") as report_file:
#         report_file.write(""" - {0}주차 주간 보고 - 
#  부서 : 
#  이름 : 
#  업무 요약 : """.format(i))


#유튜바

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간 보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약:")


