# 내 풀이
def solution(a, b):
    weekend = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0

    for i in range(a - 1):
        total += day[i]
    answer = weekend[((total + b) % 7) - 1]
    return answer

print(solution(5, 24))


# 다른 사람의 풀이
def solution_other(a, b):
    weekend = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return weekend[(sum(day[:a-1])+b-1)%7]

print(solution(5, 22))

