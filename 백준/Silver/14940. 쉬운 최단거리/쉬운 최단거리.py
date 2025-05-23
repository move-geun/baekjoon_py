import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split(' '))
maps = list(list(map(int, input().split(' '))) for _ in range(n))
ans = [[0]*(m) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
dirs = [[1,0],[-1,0],[0,-1],[0,1]]

def bfs(i,j):
    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    ans[i][j] = 0

    while q:
        x,y = q.popleft()
        for di, dj in dirs:
            nx,ny = x+di, y+dj

            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                ans[nx][ny] = ans[x][y] + 1
                q.append([nx,ny])

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == 0:
            ans[i][j] = -1

for a in ans:
    print(*a)
# print(ans)