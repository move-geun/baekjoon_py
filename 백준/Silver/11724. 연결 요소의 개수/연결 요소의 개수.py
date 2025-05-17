import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

for _ in range(m):
    sn,en = map(int, input().split(' '))
    graph[sn].append(en)
    graph[en].append(sn)

def bfs(v):
    q = deque([v])
    visited[v] = True

    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    graph[v] = []

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)