#while
# customer = "thor"
# index = 5
# while index >=1:
#     print("{0},the coffee is ready. you have {1}more chance.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("the coffee has been disposed of.")

# customer = "ironman"
# index =1
# while True:
#     print("{0}, the coffee is ready. i called you {1} times.".format(customer, index))
#     index += 1

# customer = "thor"
# person = "Unknown"

# while person != customer:
#      print("{0}, the coffee is ready.".format(customer))
#      person = input("what is your name? ")

# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("today's class is over. {0}, follow me to the office.".format(student))
#         break
#     print("{0}, read the book.".format(student))


# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I Am Groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", "Thor", "I Am Groot"]
# students = [i.upper() for i in students]
# print(students)

# Quiz) 당신은 cocoa 서비스를 이용하는 택시 기사.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성

# 조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수
# 조건2 : 당신은 소요시간 5~15분 사이의 승객만 매칭

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)

# from random import*
# a=0 #총 탑승 승객
# i=1 #몇번째 손님인지
# while i<=50:
#     b = int((random()*46)+5) #소요시간 난수
#     if b <= 15:
#         c = "O" #탑승 여부
#         a += 1 #탑승 승객 카운트
#     else:
#         c = " "
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(c, i, b))
#     i += 1
#     if i <= 50:
#         continue
#     else:
#         print("총 탑승 승객 : {0}명".format(a))
#         break #50명 채웠으니 탈출


from random import*
cnt = 0 #총 탑승 승객 수
for i in range(1, 51):
    time = randrange(5, 51) #5~50분 소요시간
    if 5 <= time <= 15: #5~15분 이내의 손님, 탑승 수 증가 처리 (매칭 성공)
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: #매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0} 명".format(cnt))