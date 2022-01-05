# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
# 예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n - 1, 3) # divmod 함수는 몫과 나머지를 튜플 데이터 타입으로 반환
        # 몫인 n이 양수일 때까진 계속 나눠서 구하는 것
        mod += 1
        if mod == 3:
            mod = 4
        rev_base += str(mod)

    return rev_base[::-1] # [::-1]은 처음부터 끝가지 -1칸 간격으로 == 역순으로
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
print(solution(500000000))
