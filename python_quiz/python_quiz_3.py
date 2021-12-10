# quiz) "사회적 거리두기"에 따른 영화관 좌석 예매 시스템

# - 각 열은 1 ~ 20번 까지 총 20개의 좌석으로 구성

# - 이 때 a열에 대해서 홀수로 끝나는 좌석에 대해서만 출력(각 좌석은 ""로 구분)

# 나
seat = []
for i in range(1,21):
    seat.append(f"A{i}")
    if i % 2 == 0:
        seat.remove(f"A{i}")
print(" ".join(seat))

# 유튜버
for i in range(1, 21)[::2]: # 2 번씩 건너뜀
    print("A" + str(i), end=" ")