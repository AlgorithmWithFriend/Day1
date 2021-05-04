def solution(s):
    length = len(s)
    index = int(length / 2)

    if length % 2 == 0:
        return s[index - 1: index + 1]
    else:
        return s[index]

print(solution("abcde"))
print(solution("opqr"))

