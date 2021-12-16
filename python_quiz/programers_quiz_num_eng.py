def solution(s):
    
    answer = []
    change_box = []
    check = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}

    for i in s:
        if i.isdigit():
            answer.append(i)
        elif i.isalpha():
            change_box.append(i)

        if "".join(change_box) in check:
            answer.append(check["".join(change_box)])
            change_box.clear()
        else:
            continue
    return int(''.join(answer))

# 오타(nine -> nien)가 있었다.......
# 풀이는 괜찮은듯?