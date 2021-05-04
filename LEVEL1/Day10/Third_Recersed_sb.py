# 풀이 실패
def convert(n):
    T = "012"
    q, r = divmod(n, 3)
    if q == 0:
        return T[r]
    else:
        return convert(q) + T[r]

def solution(n):
    answer = 0
    n = list(map(int, convert(n)));
    for i in range(len(n)):
            answer += n[i] * (3 ** i)
    return answer

n1 = 45
n2 = 125

print(solution(n1))
print(solution(n2))
