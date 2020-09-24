# 내가 해결하지 못한 풀이 ㅠㅠ
def solution(n, lost, reserve):
    for res in reserve:
        if res in lost:
            lost.remove(res)
            reserve.remove(res)
    answer = n - len(lost)
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
        elif i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
    return answer

n_1, lost_1, reserve_1 = 5, [2, 4], [1, 3, 5]
n_2, lost_2, reserve_2 = 5, [2, 4], [3]
n_3, lost_3, reserve_3 = 3, [3], [1]

print(solution(n_1, lost_1, reserve_1))
print(solution(n_2, lost_2, reserve_2))
print(solution(n_3, lost_3, reserve_3))