def solution(name):
  	# 주어진 이름에서 A가 아닌 문자의 수
    num = sum([1 if x!='A' else 0 for x in name])
    # 모두 A인 경우 (e.g., AAA)
    if not num:
        return 0
        
    # 주어진 문자에 대한 위아래 이동의 총합
    answer = sum([min(ord(x)-ord('A'), ord('Z')-ord(x)+1) for x in name])
    
    # item assignment를 위해 str에서 list로 변환
    name = list(name)

    # 인덱스 0의 경우 좌우로 이동하지 않아도 A로 만들 수 있다.
    if name[0] != "A":
        num -= 1
        name[0] = "A"
        
	# 최초 인덱스 위치는 0
    pos = 0
    # 남은 문자의 수만큼 반복
    for _ in range(num):
        for i in range(1, len(name)):
            # 원형 리스트에서 오른쪽으로 i만큼 이동한 인덱스
            r = (pos+i) % len(name)
            # 원형 리스트에서 왼쪽으로 i만큼 이동한 인덱스
            l = (pos-i) % len(name)
            
            if name[r] != "A":
                answer += i
                pos = r
                name[pos] = "A"
                break

            if name[l] != "A":
                answer += i
                pos = l
                name[l] = "A"
                break
    return answer