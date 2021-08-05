# eval함수를 통해 문자열 연산을 하면된다.
# 우리가 알고있는 연산자 우선순위가 아니다.
# 연산자 우선순위가 +가 더 크면 먼저 -크면 먼저
# 이렇게 모든 경우를 계산을 해보아서 가장 큰 값을 반환
# 문자열을 연산자랑 숫자를 분리해줘야 할 필요가 있다.
# 이를 위해 정규식으로 -+*를 한개의 그룹으로 묶어서 연산자 앞뒤로 띄어쓰기를 줌 그래서 결고를 보면 각 연산자 혹은 기호가 리스트로 들어감

import re
import itertools

def solution(expression):
    # 연산에 대한 순열
    operators = list(itertools.permutations(['-', '+', '*'], 3))
    
    # re.sub('([-+*])', ' \g<1> ', expression).split()
    expression = re.split('([-+*])', expression)
    
    result = []
    
    # 일단 먼저 - + * 순으로 연산을 해보자
    # ex) -가 expression에 있으면 100 - 200을 먼저 수행
    # 그리고 그 결과값으로 바꿔줌
    # 300 - 500도 해서 그 결과값을 바꿔주고
    # 그 다음 반복문을 돌아서 +가 있으면 연산 결과값으로 바꿔주고
    # 즉, -100-200+20 -> -100-180
    # 다음 *를 수행한 연산의 결과를 어떠한 리스트에 담아주고
    # 연산자의 우선순위를 바꿔서 결과값을 내고 리스트에 담아주고
    # 나중에 그것들에 대한 맥스값을 반환해준다.
    # 그러면 먼저 op의 이전인덱스와 다음 인덱스를 알아야한다.
    # 그러면 현재 op의 인덱스를 알아야한다.
    for operator in operators:
        # 2번째 케이스때문에.. 300이 계속 들어감
        # 한번들어가면 끝나게 해야지..
        exp = expression[:]
        for op in operator:
            while op in exp:
                idx = exp.index(op)
                # ex) 100-200
                # 단, 주의할것은 eval()은 정수를 반환하는데 다시 반복문 돌때 문자열과 연산때문에 타입에러 주의 즉, str()로 문자열 변환필요
                exp[idx-1] = str(eval(exp[idx-1] + op + exp[idx+1]))
                # 범위를 지정해서 삭제할 경우 del를 사용하면된다.
                # -100을 0번째에 넣어줬고 나머지 - 200을 지워줘야 함으로
                # 즉 idx부터 idx+1까지 지워줘야 하니까
                del exp[idx:idx+2]
        result.append(abs(int(exp[0])))
    return max(result)