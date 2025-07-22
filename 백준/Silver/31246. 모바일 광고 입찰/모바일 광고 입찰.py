import sys
import heapq

input = sys.stdin.readline
n,k = map(int, input().split())
q = []
cnt = 0
val = 0

for _ in range(n):
    s,e = map(int, input().split())
    v = e-s
    if v <= 0:
        cnt += 1
    else:
        heapq.heappush(q,v)

while cnt < k:
    tmp = heapq.heappop(q)
    
    if tmp >= val:
        val = tmp
        cnt += 1

print(val)