def solution(nums):
    
    mySet = set(nums)
    if len(mySet) > int(len(nums)/2) :
        return int(len(nums)/2)
    return len(mySet)