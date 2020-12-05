def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1))
    return answer

x1 = 2
x2 = 4
x3 = -4

n1 = 5
n2 = 3
n3 = 2

print(solution(x1, n1))
print(solution(x2, n2))
print(solution(x3, n3))