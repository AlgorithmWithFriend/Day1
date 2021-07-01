# 리스트에 숫자들의 앞을 비교하는게 우선
# 그러나 2번째 캐이스 3이 겹침

def solution(numbers):
    # 문자열로 리스트로 변환후 역순 출력
    numbers = list(map(str, numbers))
    # [999, 555, 343434, 303030, 333]
    # 앞에 3부분만 확인을 할것이므로 위의 자릿수는 무시
    numbers.sort(key=lambda x : x*3, reverse=True)
    # 이렇게 정수로 바꿨다가 문자열로 바꾼 이유는 000인 경우이기 때문
    return str(int(''.join(numbers)))