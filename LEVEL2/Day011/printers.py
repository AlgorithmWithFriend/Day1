# 큐에 관련된 문제
# 큐에서 팝해서 이게 제일 큰가 해서 아니면 뒤로 넘기고 그렇게 하는건 좋은데 location값을 구하는것이 조금 힘들었다.
# [2,1,3,2] 이때 3은 2
# [3,2,2,1] 이때 3은 0
# 해결방법으로 index값을 저장한다는 아이디어에서 시작
# index를 저장해서 index로 바꾼다.
# 우선순위는 그대로 냅둔다.

from collections import deque

def solution(priorities, location):
    indexList = deque([i for i in range(len(priorities))])
    answer = 0
    
    # 맥시멈을 처음에 priorities에서 max를 만들어낸다.
    maximum = max(priorities)
    
    while True:
        # 인덱스 리스트에서 제일 왼쪽것을 걷어낸다.
        index = indexList.popleft()
        if priorities[index] < maximum:
            indexList.append(index)
        else:
            # ex) indexList = [2,3,1,2]
            # priorities = [3,2,2,1]
            # 3을 만나면 3은 사라지고 일단 answer는 1이 된다.
            # priorities = [0,2,2,1]
            # 이제 여기서 다시 맥스값을 구한다
            answer += 1
            priorities[index] = 0
            maximum = max(priorities)
            
            # 만약 팝했을때 인덱스리스트의 그 값이 우리가 원하는 값이면
            # answer이 반환 아니면 반복문 다시 반복
            if index == location:
                return answer