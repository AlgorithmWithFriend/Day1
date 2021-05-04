# 내 풀이
from itertools import combinations

def solution(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))
    return sorted(answer)
a1 = [2,1,3,4,1]
a2 = [5,0,2,7]
print(solution(a1))
print(solution(a2))