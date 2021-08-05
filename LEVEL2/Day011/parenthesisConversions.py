# 문제에서 제시한 알로리즘을 그대로 코드로 옮기면 끝!

# 2번째 조건에서 가장 작은 균형잡힌 문자열을 찾아야한다.
# 그 위치를 찾기위한 함수를 선언해준다.
# 찾으면서 u가 올바른 괄호문자열인지 구해본다.
# 열린괄호를 left라는 변수로 카운팅
# 닫힌 괄호를 right로 카운트
# 쌍을 맞추기 위해 스택 자료구조를 이용
def parse(s):
    correct = True
    left = 0
    right = 0
    stacks = []
    
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
            stacks.append('(')
        else:
            right += 1
            # 쌍이 안 맞는경우, 즉 열린괄호가 없는경우
            if len(stacks) == 0:
                correct = False
            else:
                stacks.pop()
        # left와 right가 같아질 경우 최초로 가장 작은 길이의 균형잡힌 문자열 u가 만들어짐
        # 위치는 v의 시작위치로
        if left == right:
            return i + 1, correct
    
    # 지문에는 입력문자열이 균형잡힌 괄호문자열만 있다해서 상관없지만
    # 예외처리를 위한 부분
    return 0, False
    

def solution(p):
    if len(p) == 0:
        return p
    
    position, correct = parse(p)
    u = p[:position]
    v = p[position:]
    
    #u가 올바른 괄호문자열이면 u뒤에 붙혀서 반환
    if correct:
        return u + solution(v)
    
    answer = '(' + solution(v) + ')'
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('
            
    return answer