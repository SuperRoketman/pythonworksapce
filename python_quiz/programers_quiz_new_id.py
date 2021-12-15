import re
def solution(new_id):
    new_id = new_id.lower()
    print("1단계" + new_id)
    new_id = re.sub("[^a-z0-9-_.]","",new_id)
    print("2단계" + new_id)
    if new_id == ".": # 2번째 구멍 : .이 하나만 있으면 인덱스 에러
        new_id = new_id
    elif new_id != "." and set(new_id) == {"."}: # 1번째 구멍 : .만 있으면 인덱스 에러
        new_id = ""
    else:
        # for i in range(0, len(new_id)-1):
        #     while new_id[i] == '.' and new_id[i+1] == '.':
        #         new_id = new_id[:i] + new_id[i+1:]
        while ".." in new_id:
            new_id = new_id.replace("..", ".")

    print("3단계" + new_id)
    if new_id == ".": # 3번째 구멍 : .한개만 들어오면 인덱스 에러
        new_id = ""
    elif "." in new_id:
        while "." in new_id[0] or "." in new_id[-1]:
            if "." in new_id[0]:
                new_id = new_id[1:]
            elif "." in new_id[-1]:
                new_id = new_id[:-1]
    print("4단계" + new_id)
    if new_id == "":
        new_id = "a"
    print("5단계" + new_id)
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if "." in new_id[-1]:
            new_id = new_id[:-1]
    print("6단계" + new_id)
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    print("7단계" + new_id)
    return new_id

print(solution(new_id = "."))

# 자력으로 풀었다.
# 자꾸 오류가 나서 정답이라는 사람거 조금 보긴 했는데 결국 도움은 1도 안됐다.
# 문제가 많이 쉬운 느낌이 났다.
# 문제가 쉬운만큼 구멍도 많았다. 문제 제출하고 정답 판정까지 받았는데도 구멍이 있어서 매꿨다.
# 야미