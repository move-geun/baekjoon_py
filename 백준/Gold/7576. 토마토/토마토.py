import sys

from collections import deque

input = sys.stdin.readline
m,n = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(n)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
q = deque()
flag = False
maxi = -1

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            q.append([i,j])

def bfs():
    while q:
        x,y = q.popleft()
        for di,dj in dirs:
            nx,ny = x+di, y+dj
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==0:
                maps[nx][ny] = maps[x][y] + 1
                q.append([nx,ny])
    
bfs()

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            flag = True
        elif maps[i][j] > maxi:
            maxi = maps[i][j]

print(-1 if flag else maxi-1)
