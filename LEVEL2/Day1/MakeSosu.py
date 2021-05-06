## 처음 풀이 - combination를 이용한 풀이

from itertools import combinations

def solution(nums):
    answer = 0
    sosu = combinations(nums,3)
    for i in [sum(i) for i in sosu]:
        for j in range(2,i):
            if i%j == 0:
                break
        else: answer+=1
    return answer

## 안 좋았던 풀이 - for문 이용
def sosu(_num) :
    if _num>1:
        for i in range(2,_num):
            if _num % i == 0:
                return False
    else:
    return True

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                _num = nums[i]+nums[j]+nums[k]
                if sosu(_num) == True:
                    answer += 1
    return answer


## 2번째 풀이
from itertools import combinations 
import math;

def sosu(_num):
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    i = int(math.sqrt(_num))
    divisior = [i for i in range(1, m+1) if n % i == 0]

    return len(divisior) == 1

def solution(nums):
    sosu_num = list(combinations(nums, 3))
    enables = list(filter(lambda n: sosu(n[0] + n[1] + n[2]), sosu_num))

    return len(enables)