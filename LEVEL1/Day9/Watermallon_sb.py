def solution(n):
    answer = '수박'*(n//2)+'수'*(n%2)
    return answer

n1 = 3
n2 = 4
print(solution(n1))
print(solution(n2))
