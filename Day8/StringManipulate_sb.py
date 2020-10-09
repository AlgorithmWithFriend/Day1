def solution(s):
    answer = True

    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False
    return answer

s1 = "a234"
s2 = "1234"
print(solution(s1))
print(solution(s2))
