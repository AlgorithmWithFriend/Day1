# 풀이 실패..
def solution(strings, n):
    a = []
    answer = []
    strings.sort()
    for i in strings:
        a.append(i[n])
    a.sort()

    for i in a:
        for j in range(len(a)):
            if i == strings[j][n]:
                answer.append(strings[j])
                strings[j] = '0' * 100
    return answer

str1 = ["sun", "bed", "car"]
str2 = ["abce", "abcd", "cdx"]
n1 = 1
n2 = 2

print(solution(str1, n1))
print(solution(str2, n2))
