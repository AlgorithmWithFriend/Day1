# 입력된 두 문자열을 전부 대문자로 만들어준다.
# 다음에는 두 문자열을 2개 철자씩 묶는다.
# 묶어서 카운팅을 재준다. 묶어진 문자열이 몇개가 들어가 있는지
# ex) AA1+AA2로 보면 AA은 카운트 2개
# ex) AAAA12 는 AA 카운트 3개
# 카운팅하는 과정에서 숫자, 공백, 특수문자 같은것들이 있으면 카운팅을 하지 않는다.
# 교집합은 집합으로 만든것중 작은거
# 합집합은 큰거
# (교집합 길이 / 합집합 길이) * 65536 

def solution(str1, str2):
    # 리스트 선언
    strings = []
    # 대문자로 만들어 주기
    for string in [str1, str2]:
        converter = string.upper()
        # 문자와 카운트에 대한 딕셔너리 변수 선언
        converters = {}
        # 2개 철자로 분리
        # 핵심은 get
        # word 즉, 자기 자신 문자가 있으면 그 값에 1을 더해주고 아니면 0
        for i in range(1, len(converter)):
            word = converter[i-1] + converter[i]
            if word.isalpha():
                converters[word] = converters.get(word, 0) + 1
        strings.append(converters)
    str1, str2 = strings
    # 교집합
    interaction = []
    for s1 in str1:
        if s1 in str2:
            # 리스트 컴프리헨션 기능 사용
            interaction += [s1 for _ in range(min(str1[s1], str2[s1]))]
    
    # 합집합
    union = []
    # 키 값들만 리스트로 모아서 더해준다.
    jaccard_keys = list(str1.keys()) + list(str2.keys())
    for j in set(jaccard_keys):
        union += [j for _ in range(max(str1.get(j, 0), str2.get(j, 0)))]
    
    n = len(interaction) / len(union) if len(union) != 0 else 1
    return int(n * 65536)