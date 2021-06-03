# 먼저 남은 진도율을 스피드로 나눈 몫으로 몇일이 남았는지 스택을 만든다
# 남은 진도율은 100 - 현재 진도율
# 남은 진도율에서 스피드로 나눈 몫에서 올림처리를 저장하여 스택에 append

import math

def solution(progresses, speeds):
    _len = len(progresses)
    leftDate = []
    answer = []
    
    for i in range(_len):
        leftProgress = 100 - progresses[i]
        share = math.ceil(leftProgress / speeds[i])
        leftDate.append(share)

# ex) [7, 3, 9] 완료 일수
# left = 7이되고 스택에 빠진다 [3, 9]
# 3은 7보다 작으니까 result는 1증가 그리고 3 pop [9]
# answer = [2]
    while leftDate:
        left = leftDate.pop(0)
        result = 1
        while len(leftDate) != 0 and left >= leftDate[0]:
            result+=1
            leftDate.pop(0)
        answer.append(result)
    return answer