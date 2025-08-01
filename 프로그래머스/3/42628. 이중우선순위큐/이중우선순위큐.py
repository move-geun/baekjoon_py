import heapq

def solution(operations):
    maxq = []
    minq = []
    cnt1,cnt2 = 0,0
    for tmp in operations:
        s,n = tmp.split(' ')
        if s == 'I':
            heapq.heappush(minq, int(n))
            heapq.heappush(maxq, int(n)*-1)
        elif s == 'D' and n == '1':
            if maxq:
                tmp = heapq.heappop(maxq)*-1
                minq.remove(tmp)
                heapq.heapify(minq)
        else:
            if minq:
                tmp = heapq.heappop(minq)
                maxq.remove(tmp*-1)
                heapq.heapify(maxq)
        
    if not minq:
        return [0, 0]
    else:
        return [-maxq[0], minq[0]]


