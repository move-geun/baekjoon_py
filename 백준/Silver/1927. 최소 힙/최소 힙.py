import sys
import heapq

input = sys.stdin.readline
N = int(input())
q = []
for _ in range(N):
    a = int(input())
    if a == 0:
        if len(q):
            # 최소값 출력 및 삭제
            tmp = heapq.heappop(q)
            print(tmp)
        else:
            print(0)
    else:
        heapq.heappush(q, a)

        