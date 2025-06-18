import sys
import heapq

input = sys.stdin.readline
INF = 10**18

N, K = map(int, input().split())
MAX = 100_001

dist = [INF] * MAX
dist[N] = 0

hq = []
heapq.heappush(hq, (0, N))

while hq:
    d, x = heapq.heappop(hq)
    if d > dist[x]:
        continue
    if x == K:
        break

    # 순간이동(비용 0), 걷기(비용 1)
    for nx, w in ((x*2, 0), (x-1, 1), (x+1, 1)):
        if 0 <= nx < MAX and dist[nx] > d + w:
            dist[nx] = d + w
            heapq.heappush(hq, (dist[nx], nx))

print(dist[K])
