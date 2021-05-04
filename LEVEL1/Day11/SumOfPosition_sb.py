def solution(n):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return sum([int(i) for i in str(n)])

N1 = 123
N2 = 987

print(solution(N1))
print(solution(N2))
