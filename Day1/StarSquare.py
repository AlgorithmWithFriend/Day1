a, b = map(int, input().strip().split(' '))
if a <= 1000 and b <= 1000:
    for i in range(b):
         print("*"*a)