import heapq as hq

def solution(scoville, K):
    answer = 0
    
    # scoville 리스트를 heapq로
    hq.heapify(scoville)
    
    while True:
        # min1 : 제일 작은 맵기, min2: 두번째로 작은 맵기
        min1 = hq.heappop(scoville)
        min2 = hq.heappop(scoville)
        
        # 문제의 요구를 따라 계산 후 scoville에 추가
        hq.heappush(scoville, (min1 + min2*2))
        
        # 횟수 1회 추가
        answer += 1
        
        # 제일 작은 맵기가 K보다 크다면(다른 맵기는 모두 K보다 크므로) 횟수 return
        if scoville[0] >= K:
            return answer
        # 만약 scoville이 2개 남았고, 모든 scoville이 K보다 작다면, -1 return
        if len(scoville) == 2 and sum(scoville) < K:
            return -1