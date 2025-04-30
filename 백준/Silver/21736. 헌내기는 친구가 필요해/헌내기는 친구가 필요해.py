import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(i,j):
    cnt = 0
    q = deque([(i,j)])
    maps[i][j] = 'X'
    while q:
        x,y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] != 'X':
                if maps[nx][ny] == 'P':
                    cnt += 1
                maps[nx][ny] = 'X'
                q.append((nx,ny))
    print(cnt if cnt>0 else 'TT')


for i in range(n):
    for j in range(m):
        if maps[i][j] == 'I':
            bfs(i,j)