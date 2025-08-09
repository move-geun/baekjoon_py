from collections import deque

def solution(maps):
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    n,m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    
    def bfs(x,y):
        q = deque()
        q.append([x,y])
        visited[x][y] = 1
        
        while q:
            i,j = q.popleft()
            
            if i == n and j == m:
                return 
            
            for di,dj in dirs:
                ni,nj = i+di,j+dj
                
                if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 and maps[ni][nj] == 1:
                    q.append([ni,nj])
                    visited[ni][nj] = visited[i][j] + 1
        return -1
    
    ans = bfs(0,0)
    
    return visited[n-1][m-1] if visited[n-1][m-1] else -1