# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): #입금
#     print("the deposit has been completed. the balance is {0}KRW.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#             print("the withdrawal has been completed. the balance is {0}KRW.".format(balance - money))
#             return balance - money
#     else:
#         print("the withdrawal has failed. the balance is {0}KRW.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# a=0
# a = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("the commission is {0}KRW. the balance is {1}KRW.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("name : {0}\tage : {1}\tmain language : {2}"\
#         .format(name, age, main_lang))

# profile("YJS", 20, "Python")
# profile("KTH", 25, "Java")

# # 같은학교 같은 학년 같은 반 같은 수업 -> 기본

# def profile(name, age = 17, main_lang = "Python"):
#     print("name : {0}\tage : {1}\tmain language : {2}"\
#         .format(name, age, main_lang))

# profile("YJS")
# profile("KTH")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "YJS", main_lang = "Python", age = 20)
# profile(main_lang = "Java", age = 25, name = "KTH")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name : {0}\tage : {1}\t".format(name, age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("name : {0}\tage : {1}\t".format(name, age), end = " ")
#     for lang in language:
#         print(lang, end = " ")
#     print()


# profile("YJS", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("KTH", 25, "Kotlin", "Swift")

# gun = 10

# def checkpoint(soldiers):
#     global gun #전역 공간의 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# Quiz) 표준 체중을 구하는 프로그램을 작성

# *표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#  남자 : 키(m) * 키(m) * 22
#  여자 : 키(m) * 키(m) * 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#             * 함수명 : std_weight
#             * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.



##나
# def std_weight(height, gender):
#     a=0
#     if gender == "남자":
#         a = round(((height/100)**2)*22, 2) #round((((height/100)**2)*22)*100)/100 == round(((height/100)**2)*22, 2)
#     else:
#         a = round(((height/100)**2)*21, 2)
#     print("키 {0}cm {1}의 표준체중은 {2}kg 입니다."\
#         .format(height, gender, a))

# std_weight(172, "남자")



##유튜버
# def std_weight(height, gender): #키는 m단위 (실수), 성별은 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 22

# height = 175 #cm
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height, gender, weight))

print(round((((2/100)**2)*22)*100)/100 == round(((2/100)**2)*22, 2))