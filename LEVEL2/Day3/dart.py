import re

def solution(dartResult):
    # 변환에 대한 리스트 변수 선언
    result = []
    
    # 문자 변환에 필요한 딕셔너리
    converter = {'S':'**1', 'D':'**2', 'T':'**3', '#':'*-1'}
    
    # 1. 입력 문자열 분할
    # #이나 *은 있을수도 있고 없을수도 있기 때문에 ?붙임
    # g는 그룹을 의미 -> [SDT][*#]?를 괄호로 묶어줌
    # 그룹별로 띄어쓰기가 되면서 분할됨
    # 분할된 것을 split을 통하여 list로 반환
    divisor = re.sub('([SDT][*#]?)', '\g<1> ', dartResult).split()
    
    # 2. 분할된 문자열을 문제의 요구사항에 맞춰서  변환
    # divisor는 리스트들을 각 원소는 divide를 의미
    # 각 원소의 글자단위로 접근을 하면서 정수인지 SDT * #인지 비교를 해줘야하기 때문에 해당하는 글자까지 접근 하기위해 이중 for문
    # 1S2D*3T라는 divisor에 1S 2D* 3T라는 divide로 나누고 이 divide를 글자단위로 분리
    # 1S 2D* 3T라는 것을 1**1, 2**2*2 3**3형태로 바꿔주기 위해 replace 메소드 사용
    # SDT #은 변환 
    # 딕셔너리에 get 메소드 사용 1번째 params는 key값이고 key값이 없을 경우 2번째 params 반환
    # 스타상은 바로 전에 얻은 점수를 2배해야하는 조건 추가
    # 2배하기 전에 그 전에 앞에 값이 있는지 없는지 확인 있으면 *2문자 추가
    # result[-1] = result[-1][:-1] + '*2' 는 마지막 +문자를 빼고 *2+를 넣어준다
    # 그리고 + 문자도 추가
    for divide in divisor:
        for words in divide:
            divide = divide.replace(words, converter.get(words, words))
        if divide[-1] == '*':
            divide += '2'
            if result:
                result[-1] = result[-1][:-1] + '*2+'
        divide += '+'
        result.append(divide)
        
    # 3. 변환된 문자열의 연산값 변환
    # 문자열 자체 값을 연산하기 위해 eval() 사용
    # 문자열을 연산하기 위해 result에 값들을 문자열로 join
    # 마지막 문자열이 +인경우를 생략하가위해 [:-1] 추가
    return eval(''.join(result)[:-1])