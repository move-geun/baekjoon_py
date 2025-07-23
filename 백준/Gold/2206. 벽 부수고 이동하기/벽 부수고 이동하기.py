import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs(a,b,c):
    q = deque()
    q.append([a,b,c])
    visited[a][b][c] = 1

    while q:
        i,j,v = q.popleft()
        if i == n-1 and j == m-1:
            return visited[i][j][v]
        
        for di,dj in dirs:
            ni,nj = i+di, j+dj

            if 0<=ni<n and 0<=nj<m:
                if maps[ni][nj]==0 and visited[ni][nj][v] ==0:
                    visited[ni][nj][v] = visited[i][j][v]+1 
                    q.append([ni,nj,v])
                
                elif maps[ni][nj] == 1 and v ==0:
                    visited[ni][nj][1] = visited[i][j][v]+1
                    q.append([ni,nj,v+1])
    return -1

print(bfs(0,0,0))