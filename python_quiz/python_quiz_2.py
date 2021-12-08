# quiz) 행맨 게임 만들기

# 1. 리스트에 3개 이상의 단어를 추가
#  - apple, banana, orange

# 2. 위 리스트에서 랜덤으로 1개 단어 선택

# 3. 단어의 길이에 맞게 밑줄 출력
#  - apple = _ _ _ _ _

# 4. 사용자로부터 1 글자씩 입력을 받되, 단어에 입력값이 포함되면 correct 출력, 아니면 wrong 출력

# 5. 매번 입력 받을 때마다 현재까지 맞힌 글자들 표시 (맞히지 못한 글자는 밑줄 출력)

# 6. 정답을 맞히면 Success 출력 후 프로그램 종료(단, 횟수 제한은 없음)


# a = "a"
# b = input()
# if a == b:
#     print("correct")
# else:
#     print("wrong")

from random import *

quiz_list = []
quiz_list.append("apple")
quiz_list.append("banana")
quiz_list.append("orange") # 이렇게 한 이유 : 나중에 사전 사이트에 있는 단어들을 불러와서 쓸 수 있게 하기 위함.

answer = quiz_list[randint(0 , (len(quiz_list) - 1))] # 이렇게 한 이유 : 위와 같음

answer_list = list(answer)

hiden_answer = []
# for _ in answer_list:
#     hiden_answer.append("_")

# inputed_answer = input()
# if inputed_answer in answer_list:
#     print("Caorrect")
# else:
#     print("Wrong")



# print(answer)
# print(answer_list)
# print(''.join(answer_list))
# print(hiden_answer)
# print(' '.join(hiden_answer))

a = ["a", "a", "a", "a", "b", "b", "b", "c", "c","d", "d"]
b = []
c = []
for _ in a:
    b.append('_')
    c.append('_')

while a != c:
    inputs = input()
    i = 0
    if inputs in a:
        while i <= a.count(inputs):
            b[a.index(inputs)] = inputs
            a[a.index(inputs)] = '_'
            i += 1
    else:
        print("Wrong")
    print(a)
    print(b)
print("Success")
# while i <= a.count(inputs)+1: 일 경우 a가 3개만 지워지고 한 번 더 a를 입력 시 왜 ValueError: 'a' is not in list
# while i <= a.count(inputs)+2: 일 경우 c랑 d 입력 시 ValueError: 'c(아니면 d)' is not in list
# while i <= a.count(inputs)일 경우 3개 이상은 한 번에 못지우는가 (특정 패턴이 있음.)

# 하고싶은 것 : input이 answer_list에 있으면 answer_list의 input 값의 인덱스를 파악하고 그걸 hiden_answer 인덱스에 넣고 값을 input으로 바꿈