# 내 풀이
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num%divisor==0:
            answer.append(num)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer

arr1 = [5, 9, 7, 10]
arr2 = [2, 36, 1, 3]
arr3 = [3, 2, 6]
div1 = 5
div2 = 1
div3 = 10

print(solution(arr1, div1))
print(solution(arr2, div2))
print(solution(arr3, div3))

# 다른사람 풀이
def solution_best(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]

print(solution(arr1, div1))
print(solution(arr2, div2))
print(solution(arr3, div3))