# from random import*
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(lst)
# print("--당첨자 발표--")
# print("치킨 당첨자 : " + str(lst.pop()))
# print("커피 당첨자 : " + str(sample(lst, 3)))
# print("--축하드립니다--")

# 큰 수 리스트화 하기
# lst = range(1, 100001) #뒷자리의 숫자 직전까지..
# lst = list(lst)

from random import*
users = range(1, 21)
users = list(users)
shuffle(users)
winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")