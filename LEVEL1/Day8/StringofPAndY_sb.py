def solution(s):
    answer = True
    s = str(s).lower()
    if s.count('p') != s.count('y'):
    	return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return True

s1 = "pPoooyY"
s2 = "Pyy"

print(solution(s1))
print(solution(s2))
