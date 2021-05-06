# 첫 풀이
def solution(nums):
    
    pocketmon = set(nums)
    if len(pocketmon) > int(len(nums)/2) :
        return int(len(nums)/2)
    return len(pocketmon)

## 2번재 풀이

def solution(nums):
    pocketmon = [] # 새로운 종류의 폰켓몬을 선택하면 이 리스트에 넣음.
    for i in nums:
        try:
            if pocketmon.index(i) >= 0: # 겹치면 answer_list에 추가하지 않기
                continue
        except:
            pocketmon.append(i)
    
    if len(pocketmon) >= len(nums) / 2:
        return len(nums) / 2
    else:
        return len(pocketmon)
    
    return min(len(nums) / 2, len(pocketmon)) # len()을 활용해서 더 간략하게 수정