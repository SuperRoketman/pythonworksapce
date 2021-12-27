import math

sosu = []

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

# def solution(nums):
#     for idx1, num_f in enumerate(nums):
#         for idx2, num_s in enumerate(nums[idx1:]):
#             for num_th in nums[idx2:]:
#                 if is_prime_number(num_f + num_s + num_th):
#                     sosu.append(num_f + num_s + num_th)
#     answer = len(sosu)
#     return answer

nums = [1,2,3,4]

for idx1, num_f in enumerate(nums):
    print("num_f : ",num_f)
    nums2 = nums[idx1+1:]
    print(nums2)
    for idx2, num_s in enumerate(nums2):
        print("num_s : ",num_s)
        nums3 = nums2[idx2+1:]
        print(nums3)
        for num_th in nums3:
            print("num_th : ",num_th)
            if is_prime_number(num_f + num_s + num_th):
                sosu.append(num_f + num_s + num_th)
answer = len(sosu)
print(sosu)
print(answer)

# 무난히 풀었음. 인덱스에 + 1 을 안 해주면 왠지 적용이 안 되더라.
# 소수 찾는 알고리즘은 구글링해서 긁어옴