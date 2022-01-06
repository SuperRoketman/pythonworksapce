# signs의 길이는 absolutes의 길이와 같습니다.
# signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.


# def solution(absolutes, signs):
#     sign_hash = {True:1, False:-1}
#     i = 0
#     answer = 0
#     while i < len(absolutes):
#         answer += absolutes[i-1]*sign_hash[signs[i-1]]
#         i += 1

#     return answer
# true = True
# false = False

# print(solution([4,7,12], [true,false,true]))

# def solution(absolutes, signs):
#     i = 0
#     answer = 0
#     while i < len(absolutes):
#         answer += absolutes[i-1]*signs[i-1]
#         i += 1

#     return answer
# true = 1
# false = -1
# print(solution(	[1, 2, 3], [false, false, true]))
# 이 방법은 여기선 잘 되는데 테스트에선 안되네 왜지?

# 밑의 방법은 왠진 모르겠는데 안된다.
# 여기선 되는데 프로그래머스에선 안된다 왜지?????
# 어쨋든 위에 방법으로는 돼서 위에 방법으로 함.