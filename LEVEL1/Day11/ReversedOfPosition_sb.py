def solution(n):
    answer = list(map(int, str(n)[::-1]))
    return answer

n = 12345
print(solution(n))
