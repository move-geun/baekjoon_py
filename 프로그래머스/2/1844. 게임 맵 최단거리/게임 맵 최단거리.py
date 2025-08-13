from collections import deque

def solution(maps):
    answer = 0
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    n,m = len(maps), len(maps[0])
    maps[0][0] = 2
    q = deque()
    q.append([0,0])
    
    while q:
        x,y = q.popleft()
        for di,dj in dirs:
            ni,nj = x+di, y+dj
            
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1:
                q.append([ni,nj])
                maps[ni][nj] = maps[x][y] + 1
    
    return maps[n-1][m-1] -1 if maps[n-1][m-1] != 1 else -1
