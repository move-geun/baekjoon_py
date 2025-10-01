from collections import deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    visited = [[0]*m for _ in range(n)]
    visited2 = [[0]*m for _ in range(n)]

    def bfs(x,y,nums):
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        q2 = deque()
        q.append([x,y])
        q2.append([x,y])
        visited[x][y] = 1
        visited2[x][y] = nums
        cnt = 1
        
        while q:
            i,j = q.popleft()
            
            for di,dj in dirs:
                ni,nj = i+di, j+dj
                
                if 0<=ni<n and 0<=nj<m and visited[ni][nj] ==0 and land[ni][nj] == 1:
                    q.append([ni,nj])
                    q2.append([ni,nj])
                    visited[ni][nj] = 1
                    visited2[ni][nj] = nums
                    cnt += 1
        
        while q2:
            i,j = q2.popleft()
            land[i][j] = cnt
        
        return
    
    nums = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j,nums)
                nums += 1
                
    maxVal = 0
    for i in range(m):
        lst = set()
        prev = land[0][i]
        tmp = land[0][i]
        lst.add(visited2[0][i])
        
        for j in range(n):
            if land[j][i] != prev and visited2[j][i] not in lst:
                prev = land[j][i]
                tmp += prev
                lst.add(visited2[j][i])
                if tmp > maxVal:
                    maxVal = tmp
            elif land[j][i] == 0:
                prev = 0
    return maxVal