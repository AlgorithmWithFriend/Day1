# 풀이 실패

def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a = str(bin(a1 | a2))[2:]
        a = '0' * (n - len(a)) + a
        a = a.replace('1',"#")
        a = a.replace('0', " ")
        answer.append(a)
    return answer

n1 = 5
n2 = 6

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
arr3 = [46, 33, 33, 22, 31, 50]
arr4 = [27, 56, 19, 14, 14, 10]

print(solution(n1,arr1,arr2))
print(solution(n2,arr3,arr4))