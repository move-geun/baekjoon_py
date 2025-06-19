import sys
import heapq

input = sys.stdin.readline
INF = 1e9
v,e = map(int, input().split())
k = int(input())
dist = [INF]*(v+1)
maps = [[] for _ in range(v+1)]

for _ in range(e):
    v,e,w = map(int, input().split())
    maps[v].append((e,w))

q = []
dist[k] = 0
heapq.heappush(q, (0,k))

while q:
    cost, cur = heapq.heappop(q)

    if cost > dist[cur]:
        continue

    for next, nval in maps[cur]:
        tmp = cost+nval

        if dist[next] <= tmp:
            continue
        dist[next] = tmp
        heapq.heappush(q, (tmp, next))

for i in dist[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)