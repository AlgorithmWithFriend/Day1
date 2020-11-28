def solution(num):
    answer = 0
    
    for i in range(500):
        if num == 1:
            return answer
        else:
            if num % 2 == 0:
                num = num // 2
                answer += 1
            else:
                num = num * 3 + 1
                answer += 1
    return -1

n1 = 6
n2 = 16
n3 = 626331

print(solution(n1))
print(solution(n2))
print(solution(n3))