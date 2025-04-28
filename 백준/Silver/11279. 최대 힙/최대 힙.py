import sys
import heapq

input = sys.stdin.readline
t = int(input())
q = []
for _ in range(t):
    tmp = int(input())
    if tmp == 0:
        if len(q):
            # 최대값
            num = heapq.heappop(q)
            print(num*-1)
        else:
            print(0)
    else:
        heapq.heappush(q, tmp*(-1))
