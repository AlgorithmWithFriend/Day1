def solution(x):
    answer = x % sum([int(i) for i in str(x)]) == 0
    return answer

arr1 = 10
arr2 = 12
arr3 = 11
arr4 = 13

print(solution(arr1))
print(solution(arr2))
print(solution(arr3))
print(solution(arr4))