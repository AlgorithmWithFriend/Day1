# 첫 글자는 무조건 스택에 담는다
# 이후 두번째 글자부터 for문을 진행한다
# for문을 진행하면서 stack의 top에 있는 글자와 현재 글자가 갔다면 stack을 pop 해준다
# 같지 않다면 스택에 push한다.
# 위에 과정을 거쳐서 스택이 비면 answr는 1로 한다.

def solution(s):
    answer = 0
    
    charList = []
    
    charList.append(s[0])
    
    for i in range(1, len(s)):
        if charList == []:
            charList.append(s[i])
            continue
        
        if charList[-1] == s[i]:
            charList.pop()
            continue
        
        charList.append(s[i])
    
    if charList == []:
        answer = 1
    
    return answer