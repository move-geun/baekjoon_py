import sys
import heapq

input = sys.stdin.readline
INF = 1e9
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    st,et,v = map(int, input().split())
    graph[st].append([v,et])

def dikstra(start, end):
    q = []
    dist = [INF]*(n+1)
    dist[start] = 0
    heapq.heappush(q, [0, start])
    
    while q:
        val, cur = heapq.heappop(q)

        if dist[cur] < val:
            continue

        for nval, next in graph[cur]:
            if dist[next] > dist[cur]+nval:
                dist[next] = dist[cur]+nval
                heapq.heappush(q,[dist[next], next])
    
    return dist[end]

maxv = -INF

for i in range(1,n+1):
    tmp = dikstra(i, x)
    tmp += dikstra(x, i)
    maxv = max(maxv, tmp)

print(maxv)