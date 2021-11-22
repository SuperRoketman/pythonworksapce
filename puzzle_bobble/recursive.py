# 재귀 함수 호출
# for i in range(1, 6):
#     print(i)
#     if i == 5:
#         print("번호 끝")

# def count_1(): # 첫 번째 군인
#     print(1)
#     count_2()
#     print("1 끝")

# def count_2(): # 두 번째 군인
#     print(2)
#     count_3()
#     print("2 끝")


# def count_3():
#     print(3)
#     count_4()
#     print("3 끝")

# def count_4():
#     print(4)
#     count_5()
#     print("4 끝")


# def count_5():
#     print(5)
#     print("번호 끝")
#     print("5 끝")


# # count_1()

# def count(num):
#     print(num)
#     if num == 5:
#         print("번호 끝")
#     else:
#         count(num + 1)
#     print(num, "끝")

# count(1)

############################################################

# Quiz) 팩토리얼을 구하는 재귀함수를 작성
# - 팩토리얼 : 주어진 수보다 작거나 같은 모든 양의 정수의 곱
#     n! = n(n-1)(n-2)(n-3)(n-4)*...1

# 힌트
# 1) n! = n(n-1)!
# 2) 1! = 0! = 1

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    elif n == 1:
        return 1

result = factorial(4)
print(result) # 24