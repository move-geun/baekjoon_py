import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
maps = [[0]*(m+2)]

for _ in range(n):
    row = [0] + [int(c) for c in input().strip()] + [0]
    maps.append(row)
maps.append([0]*(m+2))

d = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(j,i):
    q = deque([(j,i)])
    while q:
        y,x = q.popleft()
        for dj,di in d:
            ny,nx = y+dj, x+di
            if 1<=ny<=n and 1<=nx<=m and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny,nx))

bfs(1,1)
print(maps[n][m])
