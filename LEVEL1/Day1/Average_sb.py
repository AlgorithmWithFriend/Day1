def solution(arr):
    if not len(arr):
        return 0
    answer = sum(arr) / len(arr)
    return answer

arr = [1,5,4,8]
print("{}".format(solution(arr)))
