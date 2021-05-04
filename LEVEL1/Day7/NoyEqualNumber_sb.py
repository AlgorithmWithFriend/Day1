def solution(arr):
   answer = []
   for i in range(len(arr)):
       if( i == len(arr)- 1):
           answer.append(arr[i])
       else:
           if (arr[i] != arr[i+1]):
            answer.append(arr[i])
   return answer

a1 = [1, 1, 3, 3, 0, 1, 1]
a2 = [4, 4, 4, 3, 3]

print(solution(a1))
print(solution(a2))

