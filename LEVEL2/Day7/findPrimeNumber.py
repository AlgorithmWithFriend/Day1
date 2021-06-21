# 1. 어떤 숫자가 소수인지 판별해주는 작업이 필요함 -> 함수로 따로 생성 !
# 2. 입력 받은 numbers ('17' 등등)을 정수형 숫자로 조합 할 수 있는 모든 경우를 조합해야함 -> itertools의 permutations (순열) 모듈 사용 !
# 3. 조합된 모든 숫자들을 소수 판별 함수로 검사하여 개수를 세면 끝 !

import math
import itertools

def isPrime(n):
    if n < 2: return False
    
    m = int(math.sqrt(n)) + 1
    for i in range(2, m):
        if n % i == 0: return False
    return True

def solution(number):
    result = set()
    
    for i in range(len(number)):
        numbers = set(map(int, map(''.join,itertools.permutations(number, i+1))))
        result |= numbers # 합집합
    
    answer = 0
    result = list(result) # 리스트 변환
    for n in result:
        if isPrime(n):
            answer += 1
    return answer