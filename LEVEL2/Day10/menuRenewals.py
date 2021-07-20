# orders에서 course의 배열로 코스요리를 만든다.
# 즉, 1번째 예시처럼 2개짜리 코스요리, 3개짜리, 4개짜리 코스요리 개발
# orders에서 하나하나 세본다.  가장 많은것이 result로 들어간다.
# 만약 가장 많은것들이 동일한 개수로 있는경우 둘다 들어간다.
# 단, 하나하나 세어서 확인하는것은 조금 비효율적인 방법
# 여기서 힌트는 문자열의 등장횟수를 세는것이다.
# 나올수 있는 모든 애들에 대해서 히스토그램을 저장한다.
# 단, 길이에 따라 다르게 저장한다.(ex. 2개일때 3개일때 4개일때)
# 히스토그램에서 가장 큰값을 뽑고 리스트에 넣어주면 끝!
# 즉, 각 문자열에 대해서 카운트값을 증가시켜주는것이다.
# 그리고 "ABCFG"에서 2개, 3개, 4개를 뽑는경우는 콤비네이션 모듈 사용
# 단, 주의할께 콤비네이션은 n이 커질수록 값이 엄청 커지기 때문에 주의
# 여기서 컴비네이션을 적용할지 고민... 경우의수가 10만개는 안넘기때문에 일단 사용
# why? 10C5가 가장 큰 경우이기때문인데 이 값이 각각의 오더에 경우에 생각해도 충분..
# 각 코스에 대한 테이블을 만든다

import itertools

def solution(orders, course):
    table = {}
    # 2개짜리 3개짜리 4개짜리에 대한 딕셔너리 생성
    for i in course:
        table[i] = {}
    for j in orders:
        for i in course:
            for comb in itertools.combinations(j, i):
                # comb: 'A', 'B'... 메뉴가 담긴다.
                # join을 통해 메뉴로 만들어준다.
                # 합칠때 주의할점은 오름차순으로 정렬되어야한다고 했으므로 sorted로 정렬해준다.
                # BA가 나올때 AB로 해준다
                # 또한 메뉴가 생길때마다 생성해서 넣어준다
                menu = "".join(sorted(comb))
                # 메뉴가 없으면 값을 생성해서 넣어주고 있으면 값 증가
                if menu not in table[i].keys():
                    table[i][menu] = 1
                else:
                    table[i][menu] += 1
    # 이게 히스토그램중에 값이 가장 큰 값을 answer에 넣어준다
    answer = []
    
    for i in course:
        # 테이블에 원소가 없을 경우
        if len(table[i]) == 0:
            continue
        bigNum = max(table[i].values())
        # 최소 손님 2명이상이 주문한것만 후보포함조건때문에 이 분기 걸어야함
        if bigNum < 2:
            continue
        for key in table[i].keys():
            # 큰 값을 찾으면
            # 또한 bigNum이 하나면 아래 조건절에 break를 걸어서 끝내겠지만 여러개일수 있으므로..
            if bigNum == table[i][key]:
                # 여기서 키값은 메뉴이다.
                answer.append(key)
    return sorted(answer)