def solution(lottos, win_nums):
    win = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    최고순위 = win[len(set(lottos)&set(win_nums)) + lottos.count(0)]
    최저순위 = win[len(set(lottos)&set(win_nums))]
    
    
    return 최고순위, 최저순위

# 프로그래머스에서 푼 첫 문제. 이런 문제 푸는게 처음이다보니
# 어떻게 해야할지 몰라서 질문 창을 조금 찾아봤는데
# 너무 뇌리에 박히는 강력한 풀이가 있어서 다른 방법을 도저히 생각할 수가
# 없었다. 최근에 Hash에 대해 알게돼서 더욱 그런 것 같다.
# 참 대단한 사람들이 많은 것 같다.