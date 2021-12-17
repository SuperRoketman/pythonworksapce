# 왼엄지는 * / 오른엄지는 #에서 시작
# 엄지는 상하좌우 4가지 방향으로만 이동 가능 / 이동 거리는 1
# 왼쪽 3열의 숫자 1, 4, 7은 무조건 왼엄지
# 오른 3열의 숫자 3, 6, 9는 무조건 오른엄지
# 가운대의 2, 5, 8, 0 은 가까운거 / 거리가 같을 시 오른손잡이는 오른손으로 왼손잡이는 왼손으로

def locate_i(i):
    pass




numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"



L_location = ["*"]
R_location = ["#"]

LR_move = []

num_pad = [[1], [2], [3]],[[4], [5], [6]], [[7], [8], [9]], [["*"], [0], ["#"]]


# rule = {1:"l", 4:"l", 7:"l", 3:"r", 6:"r", 9:"r"}

# for i in numbers:
#     if i in rule:
#         if rule[i] == "l":
#             LR_move.append("l")
#             L_location.append(i)
#         elif rule[i] == "r":
#             LR_move.append("r")
#             R_location.append(i)
#     else:

print(num_pad.index(0,0))