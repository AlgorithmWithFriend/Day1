from collections import Counter

def solution(lottos, win_nums):
    lotto = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    c = Counter(lottos) - Counter(win_nums)
    cnt = 6 - sum([v for k, v in c.items()])
    return [lotto[cnt+c[0]], lotto[cnt]]