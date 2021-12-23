def solution(numbers):

    a = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = set([])
    b.update(numbers)
    print(b)
    return sum(a-b)

# 넘버의 길아 : 1 ~ 9
# 넘버의 수 : 0 ~ 9
# 넘버는 모든 수 다름.
# 넘버 입력은 리스트

a = solution([1,2,3,4,6,7,8,0])
print(a)

# 그냥 무난히 쉬웠음. 코딩 처음 배울 때 풀었던 문제들 정도