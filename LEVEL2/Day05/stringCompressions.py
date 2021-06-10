import re

def solution(s):
    # 길이가 2개인 경우를 생각
    if len(s) <= 2:
        return len(s)
    
    # 문자열의 절반까지 반복문을 돌린다.
    # 이때 잘라준 문자열을 담을 리스트를 만든다.
    # sub 함수를 통해 s라는 문자열에  (\w{%i})있으면 \g<1>로 대신한다. \w는 글자를 나타내는데 글자가 1개가 있으면 1개의 그룹으로 나타낸다. 그리고 띄어쓰기를 기준으로 split을 해서 리스트에 담은다. 즉, 1개일때, 2개일때.. 절반까지 리스트에 담긴다.
    # 앞의 글자랑 다음 글자랑 일치하는지 비교를 한다. 일치를 하면 카운트를 세어준다. 그리고 마지막에 카운트를 앞에 붙여준다.
    # 단, a,a,b인 경우를 생각하여 else문에 분기를 한번 나눠준다.
    resultCount = [] # 각각의 길이를 카운트해서 리스트에 담는다.
    for i in range(1, len(s) // 2 + 1):
        strList = re.sub('(\w{%i})' %i, '\g<1> ', s).split()
        count = 1
        result = [] # 변환된 문자를 담아줄 리스트이다.
        for j in range(len(strList)):
            if j < len(strList)-1 and strList[j] == strList[j+1]:
                count += 1
            else:
                if count == 1:
                    result.append(strList[j])
                else:
                    result.append(str(count) + strList[j])
                    count = 1
        # 카운트를 셀때 문자열로 조인한 결과를 append
        resultCount.append(len(''.join(result)))
    return min(resultCount)
        
        