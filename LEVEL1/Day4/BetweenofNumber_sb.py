def solution(a, b):
    answer = sum(range(min(a,b), max(a,b) + 1))
    return answer

n_1 = 3
n_2 = 3
n_3 = 5

m_1 = 5
m_2 = 3
m_3 = 3

print(solution(n_1, m_1))
print(solution(n_2, m_2))
print(solution(n_3, m_3))