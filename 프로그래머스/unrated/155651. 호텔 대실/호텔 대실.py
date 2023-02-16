from heapq import heappop, heappush

def solution(book_time):
    answer = 1          # 방 하나부터 시작

    # 비교가능한 숫자로 변경
    book_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_ref.sort()
    
    heap = []
    for s, e in book_ref:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)
    
    return answer