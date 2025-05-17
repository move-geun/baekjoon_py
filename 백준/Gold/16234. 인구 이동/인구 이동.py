import sys
from collections import deque

input = sys.stdin.readline
N,L,R = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(N)]

dirs = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(i,j):
    union = []
    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    union.append([i,j])

    while q:
        x,y = q.popleft()
        for di, dj in dirs:
            nx,ny = x+di, y+dj
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and L <= abs(maps[x][y] - maps[nx][ny]) <= R:
                visited[nx][ny] = 1
                union.append([nx,ny])
                q.append([nx,ny])
    
    if len(union) <= 1:
        return 0
    else:
        member = sum(list(maps[mi][mj] for mi,mj in union))//len(union)
        for ui, uj in union:
            maps[ui][uj] = member
    return 1
day = 0
while True:
    cnt = 0
    visited = [[0]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                cnt += bfs(i,j)
                visited[i][j] = 1
    if cnt == 0:
        break
    day += 1

print(day)
