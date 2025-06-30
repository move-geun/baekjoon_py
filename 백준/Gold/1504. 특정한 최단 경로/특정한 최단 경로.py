import sys
import heapq

input = sys.stdin.readline
n,m = map(int, input().split())
INF = 1e9

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

st,et = map(int, input().split())

def dikstra(num, tar):
    dist = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0,num))
    dist[num] = 0

    while q:
        val, cur = heapq.heappop(q)

        if dist[cur] < val:
            continue

        for next,nval in graph[cur]:
            tmp = nval+val
            if dist[next] > tmp:
                dist[next] = tmp
                heapq.heappush(q, (tmp, next))
    return dist[tar]

ans1 = dikstra(1,st) + dikstra(st,et) + dikstra(et,n)
ans2 = dikstra(1,et) + dikstra(et,st) + dikstra(st,n)
tmp = min(ans1, ans2)

print(-1 if tmp >= INF else tmp)
