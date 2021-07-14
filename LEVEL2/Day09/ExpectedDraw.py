# N 은 2의 지수승으로 주어지기 때문에 2진수와 관련이 있지 않을까 생각했다.
# 8팀이 주어졌을때 2번과 7번이 만나기 위해서는 총 3번의 경기를 진행해야한다.
# 예시로 든것처럼 노가다를 해본다. a와 b가 같아질때 까지
def solution(n,a,b):
    answer = 0
    while a!=b:
        if a%2==0:
            a//=2
        else:
            a//=2
            a+=1
        if b%2==0:
            b//=2
        else:
            b//=2
            b+=1
        answer+=1
    return answer