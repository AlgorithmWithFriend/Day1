
# 3진법을 이용 3으로 나눴을 때 나머지값을 이용할건데, 0부터 시작해야하므로 n - 1을 해주고 시작
# n이 3보다 작은값을 만났을때 나머지값을 리스트 [1,2,4] 인덱스로 접근하여 결과값 반환
# n이 3보다 크면 반복문을 이용해 몫을 n으로두고 반복
def solution(n):
    answer = ''
    num = [1,2,4]
    while n > 0:
        n -= 1
        answer = str(num[n%3]) + answer
        n = n//3
    return answer