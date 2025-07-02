import sys
from collections import deque

input = sys.stdin.readline
m,n,k = map(int, input().split())
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
maps = [[0]*(n) for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            maps[i][j] = 1

def bfs(x,y,cnt):
    q = deque()
    ans = 1
    maps[x][y] = cnt
    q.append([x,y])

    while q:
        i,j = q.popleft()
        for dx,dy in dirs:
            nx,ny = i+dx, j+dy

            if 0<=nx<m and 0<=ny<n and maps[nx][ny] == 0:
                ans += 1
                maps[nx][ny] = cnt
                q.append([nx,ny])
    return ans


tmp = 1
ans = []

for i in range(m):
    for j in range(n):
        if maps[i][j] == 0:
            ttmp = bfs(i,j,tmp)
            ans.append(ttmp)
            tmp += 1
ans.sort()
print(tmp-1)
print(*ans)