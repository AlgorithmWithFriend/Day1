def solution(n):
    answer = 0
    temp = n
    tempList = []
    while temp != 0:
        tempList.append(temp % 10)
        temp = temp // 10
    tempList.sort()
    tempList.reverse()
    tempStr = ''
    for i in tempList:
        tempStr += str(i)

    answer = int(tempStr)
    return answer

n = 118372
print(solution(n))
