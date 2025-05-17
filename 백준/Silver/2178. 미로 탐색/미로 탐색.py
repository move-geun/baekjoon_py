import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int, input().split(' '))
maps = [list(map(int, input().strip())) for _ in range(N)]
n,m = N-1, M-1
dirs = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(i,j):
    q = deque([(i,j)])
    cnt = 2
    maps[i][j] = cnt

    while q:
        x,y = q.popleft()
        for di,dj in dirs:
            nx,ny = x+di, y+dj
            if 0<=nx<N and 0<=ny<M and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append([nx,ny])
    
bfs(0,0)

print(maps[n][m]-1)
