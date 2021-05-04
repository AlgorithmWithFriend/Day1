def solution(n):
    answer = [n]
    n1 = int(n / 2)
    while n1 >= 1:
        if n % n1 == 0:
            answer.append(n1)
        n1 -= 1
    return sum(answer)

n1 = 12
n2 = 5

print(solution(n1))
print(solution(n2))
