import heapq
def solution(n, k, enemys):
    answer = 0
    q = []
    for enemy in enemys:
        if n >= enemy:
            n -= enemy
            heapq.heappush(q, -enemy)
        else:
            if k < 1:
                break
            else:
                n -= enemy
                k -= 1
                heapq.heappush(q, -enemy)
                num = -heapq.heappop(q)
                n += num
        answer += 1
    return answer