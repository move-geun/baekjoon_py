import sys
import heapq

input = sys.stdin.readline
INF = 1e9
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ans = INF
ans_lst = []

for _ in range(m):
    st,et = map(int, input().split())
    graph[st].append([1,et])
    graph[et].append([1,st])

def dikstra(a):
    dist = [INF]*(n+1)
    q = []
    dist[a] = 0
    heapq.heappush(q,[0,a])

    while q:
        val, cur = heapq.heappop(q)

        if dist[cur] < val:
            continue

        for nval, next in graph[cur]:
            if dist[next] > dist[cur]+nval:
                dist[next] = dist[cur]+nval
                heapq.heappush(q, [dist[next], next])
    return dist[1:]

tmp = dikstra(1)

for i in range(n):
    if tmp[i] == INF:
        tmp[i] = -1

maxV = max(tmp)
print(f'{tmp.index(maxV)+1} {maxV} {tmp.count(maxV)}')

