def solution(s):
    answer = ''
    idx = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if idx % 2 == 0:
                answer += s[i].upper()
            else : answer += s[i].lower()
            idx += 1
        else :
            idx = 0
            answer += ' '
    return answer

s = "try hello world"
print(solution(s))
