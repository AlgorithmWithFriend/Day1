def solution(s):
    answer = "".join(sorted(s)[::-1])
    return answer

s = "ProgRam"
print(solution(s))
