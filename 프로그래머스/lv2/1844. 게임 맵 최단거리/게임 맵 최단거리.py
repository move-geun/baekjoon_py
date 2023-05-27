from collections import deque

def solution(maps):
    n,m = len(maps), len(maps[0])
    dir = [(-1,0),(0,1),(1,0),(0,-1)]
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    
    while q:
        y,x = q.popleft()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1:
                if visited[ny][nx] == 0:
                    maps[ny][nx] = maps[y][x] + 1
                    visited[ny][nx] = 1
                    q.append([ny,nx]) 
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1] 