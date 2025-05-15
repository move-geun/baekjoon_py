import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split(' '))
answer = []
graph = list([] for _ in range(n+1))
for _ in range(m):
    sn, en = map(int, input().split(' '))
    graph[sn].append(en)
    graph[en].append(sn)

def BFS(i):
    visited = [0] * (n+1)
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        t = q.popleft()
        for v in graph[t]:
            if not visited[v]:
                visited[v] = visited[t]+1
                q.append(v)
    return sum(visited)

for i in range(1, n+1):
    answer.append(BFS(i))

print(answer.index(min(answer))+1)
