import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1 and scoville[0] < K:
        tmp = heapq.heappop(scoville)
        tmp2 = heapq.heappop(scoville)
        heapq.heappush(scoville, tmp+tmp2*2)
        answer += 1
    return answer if scoville[0] >= K else -1

