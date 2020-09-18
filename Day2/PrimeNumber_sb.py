def solution(n):
    primeNumber = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if primeNumber[i] == True:
            for j in range(2*i, n+1, i):
                primeNumber[j] = False
    answer = len([i for i in range(2, n+1) if primeNumber[i] == True])

    return answer

print(solution(10))