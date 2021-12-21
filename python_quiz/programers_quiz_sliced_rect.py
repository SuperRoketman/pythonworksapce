import math

def solution(w,h):
    s = 0

    m = math.gcd(w, h)

    m_w = int(w/m)
    m_h = int(h/m)

    if w == 1 or h == 1:
        return 0

    else:
        if m_h/m_w % 1 != 0:
            s += 1 + math.trunc(m_h/m_w)
            # print("if, if", i, s)
        elif m_h/m_w % 1 == 0:
            s += math.trunc(m_h/m_w)  
            # print("if, else", i, s)

        for i in range(2, m_w + 1):
            if m_h*i/m_w % 1 != 0:
                s += 1 + math.trunc(m_h*i/m_w) - math.trunc(m_h*(i-1)/m_w)
                # print("else, if", i, s)
            elif m_h*i/m_w % 1 == 0:
                s += math.trunc(m_h*i/m_w) - math.trunc(m_h*(i-1)/m_w)  
                # print("else, else", i, s)
        return(w*h-s*m)

print(solution(99999999, 1))







# 아직 푸는 중, 풀이는 맞는데 자꾸 시간초과가 뜨네,,,, 개같은거
# 21.12.21.19:34 풀었음. 계속 한 가지 유형에서 시간초과가 떠서 왜 안되지 싶었는데 맨 처음에 w 나 h 가 1일 경우를 해두지 않으면 w = 99999999 / h = 1 이렇게 뜨면 오래걸리나보다 실제로 해보니
# 개오래걸림. 1분정도 걸린듯 / 정답식으로 똑같이 해보니 1초도 안 걸림.
# 어쨌든 끝