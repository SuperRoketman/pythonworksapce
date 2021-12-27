completion = [1, 2, 3]
participant = [3,2,1,4]

completion.sort()
completion.append(0)
participant.sort()

for i in range(len(participant)):
    if participant[i] != completion[i]:
        a = participant[i]
        break   
    
print(a)

# 그냥저냥 어렵지 않았다.
# completion에 0을 추가해서 길이를 맞추는건 질문하기 참고했다...ㅎㅎ