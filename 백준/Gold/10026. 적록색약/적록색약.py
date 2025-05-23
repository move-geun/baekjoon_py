import sys

from collections import deque

input = sys.stdin.readline
n = int(input())
maps = [list(input().strip()) for _ in range(n)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
visited1 = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]

def bfs(i,j,color):
    q = deque()
    q.append([i,j])
    visited1[i][j] = 1

    while q:
        x,y = q.popleft()
        for di,dj in dirs:
            nx,ny = x+di, y+dj
            
            if 0<=nx<n and 0<=ny<n and visited1[nx][ny]==0 and maps[nx][ny] == color:
                visited1[nx][ny] = 1
                q.append([nx,ny])

def bfs2(i,j,color):
    q = deque()
    q.append([i,j])
    visited2[i][j] = 1

    while q:
        x,y = q.popleft()
        for di,dj in dirs:
            nx,ny = x+di, y+dj
            
            if 0<=nx<n and 0<=ny<n and visited2[nx][ny]==0:
                if color == 'R' or color == 'G':
                    if maps[nx][ny] == 'R' or maps[nx][ny] == 'G':
                        visited2[nx][ny] = 1
                        q.append([nx,ny])
                else:
                    if maps[nx][ny] == 'B':
                        visited2[nx][ny] = 1
                        q.append([nx,ny])

cnt1, cnt2 = 0,0

for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            cnt1 += 1
            bfs(i,j,maps[i][j])
        if visited2[i][j] == 0:
            cnt2 += 1
            bfs2(i,j,maps[i][j])

print(cnt1, cnt2)
