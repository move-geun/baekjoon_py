import sys
import heapq

input = sys.stdin.readline
INF = 1e9
n = int(input())
graph = [[] for _ in range(n+1)]
ans = INF
ans_lst = []

while True:
    st,et = map(int, input().split())
    if st == -1 and et == -1:
        break
    graph[st].append([1, et])
    graph[et].append([1, st])

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

for i in range(1,n+1):
    tmp = dikstra(i)
    mval = max(tmp)

    if ans > mval:
        ans_lst = []
        ans = mval
        
    if ans == mval:
        ans_lst.append(i)

print(f'{ans} {len(ans_lst)}')
print(*ans_lst)
