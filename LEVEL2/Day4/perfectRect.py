# 유클리드 호제법으로 최대공약수 구하기
# 이 부분만 참고
def gcd(a, b): 
    if a < b: 
        (a, b) = (b, a) 
    while b != 0: 
        (a, b) = (b, a % b) 
    return a

def solution(w,h):
    answer = w * h - w - h + gcd(w, h)
    return answer