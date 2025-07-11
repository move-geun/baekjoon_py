import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
time = 0

def airs(i,j):
    q = deque()
    q.append([i,j])
    visited[i][j] = 1

    while q:
        x,y = q.popleft()
        for di,dj in dirs:
            ni,nj = x+di, y+dj

            if 0<=ni<n and 0<=nj<m:
                if visited[ni][nj] == 0 and maps[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append([ni,nj])
                elif maps[ni][nj] == 1:
                    visited[ni][nj] += 1


while True:
    visited = [[0]*(m) for _ in range(n)]
    airs(0,0)

    time += 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                maps[i][j] = 0
    
    air = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                air += 1
    
    if air == (n*m):
        break

print(time)