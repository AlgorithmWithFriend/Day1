def solution(arr):
    del arr[arr.index(min(arr))]
    if len(arr) == 0:
        arr.append(-1)
    return arr

arr1 = [4,3,2,1]
arr2 = [10]

print(solution(arr1))

print(solution(arr2))
