# 스코빌 : 리스트
# K : int
# return : int
# K 로 만들 수 없는 경우 -1을 return

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 
# + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞음


# 한 번 섞을 때마다 스코빌의 길이는 1씩 짧아짐
# 길이가 1이 될때까지 K를 넘지 않으면 연산을 100만번 해야하고
# 이건 10초가 넘어감.


import heapq

def solution(scoville, K):
    scoville.sort()
    stack = 0

    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (min1 + (min2*2)))
            # scoville.append(scoville[0] + (scoville[1]*2))
            # scoville = scoville[2:]
            # scoville.sort()
            stack += 1



    return scoville, stack





print(solution([1,2,3,9,10,12], 7))




# 이번에 heapq 라는 모듈에 대해서 알게되었다.
# heapq는 O(logN) 의 시간복잡도를 가져 큰 수일수록 효율적으로 가능
# heapq는 리스트가 정렬된 상태로 작동됨.