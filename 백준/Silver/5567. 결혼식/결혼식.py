import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
fr = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    fr[a].append(b)
    fr[b].append(a)

q = deque()
q.append([1,0])
visited[1] = 1

while q:
    x,cnt = q.popleft()

    if cnt >= 2:
        continue

    for y in fr[x]:
        if visited[y]==0:
            visited[y] = 1
            q.append([y, cnt+1])

ans = 0
for i in visited[2:]:
    if i == 1:
        ans += 1

print(ans)

