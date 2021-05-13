def solution(N, stages):
    answer = []
    _len = len(stages)
    _num = 0
    
    for x in range(1, N+1):
        for y in stages:
            if x==y:
                _num+=1
        if _num > 0:
            answer.append(_num/_len)
            _len = _len - _num
            _num = 0
        else:
            answer.append(0)
    answer = sorted(range(len(answer)), key=lambda k : answer[k], reverse=True)
    answer = [x+1 for x in answer]
    return answer