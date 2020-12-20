def solution(d, budget):
    answer = 0
    d.sort()
    
    for dVal in d:
        budget -= dVal
        answer += 1
        if budget < 0:
            break
    
    if budget >= 0:
        return answer
    else:
        return answer -1

d1 = [1,3,2,5,4]
d2 = [2,2,3,3]

budget1 = 9
budget2 = 10

print(solution(d1, budget1))
print(solution(d2, budget2))