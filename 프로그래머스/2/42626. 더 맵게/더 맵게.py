import heapq

def solution(scoville, K):
    
    heap = []
    answer = 0
    
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])
    
    
    min1 = heapq.heappop(heap)
    min2 = heapq.heappop(heap)
    
    while min1 < K:
           
        sum_food = min1 + min2 * 2
        heapq.heappush(heap, sum_food)
        answer += 1
        
        if len(heap) >= 2 :
            min1 = heapq.heappop(heap)
            min2 = heapq.heappop(heap)   
        else:
            if len(heap) == 1:
                if heapq.heappop(heap) > K:
                    return answer
            return -1;
        
    
    return answer