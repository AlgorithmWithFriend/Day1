# 먼저 접두어를 찾는게 핵심
# 첫 번째 문자를 가진 것들끼리 묶는다.
# 첫번째 문자가 딕셔너리에 담겨져 있다면
# out: {'1':['119', '1195524421'], '9':['97674223']}
# 단, 원소의 길이가 1이면 접두어가 될수 없기때문에 길이가 2이상인것을 찾아야한다.
# 1이상인경우는 관심이 없고 반복문은 계속 돌아야하기때문에 continue를 사용
# 길이가 짧은게 더 긴거에 접두어가 되어야한다.
def solution_fail(phone_book):
    dic = {}
    
    for phone in phone_book:
        if phone[0] not in dic.keys():
            dic[phone[0]] = [phone]
        else:
            dic[phone[0]].append(phone)
    for k in dic.keys():
        if len(dic[k]) == 1:
            continue
        elif len(dic[k]) > 1:
            for i in range(len(dic[k])):
                for j in range(len(dic[k])):
                    if len(dic[k][i]) < len(dic[k][i]) and dic[k][j][:len(dic[k][i])] == dic[k][i]:
                        return False
    return True

# 입력을 딕셔너리형태로 바꾼다.
# 하나씩 돌면서
# ex) 1195524421에서 1, 11, 119.. 이렇게 커가면서 해시맵에 이 값이 존재하는지 여부를 정한다.
# 119가 해시맵에 존재하니까 False 단, 똑같을 경우 예외처리

def solution_success(phone_book):
    dic = {}
    for phone in phone_book:
        # 해시맵에 정보저장
        dic[phone] = 1
    for phone in phone_book:
        # 하나씩 늘려가는것을 저장하기 위한 임시변수
        temp = ""
        for num in phone:
            temp+=num
            if temp in dic and temp != phone:
                return False
    return True 