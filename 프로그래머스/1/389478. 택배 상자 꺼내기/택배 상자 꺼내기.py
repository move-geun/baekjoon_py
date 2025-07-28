from collections import deque

def solution(n, w, num):
    answer = 0
    dirs = [[0,1],[-1,0],[0,-1],[-1,0]]
    rows = n//w + (1 if n%w else 0)
    visited = [[0]*w for _ in range(rows)]
    maps = [[0]*w for _ in range(rows)]
    
    def tmp(rows):
        start = 1
        d = -1
        i,j = rows-1,0
        maps[i][j] = start
        visited[i][j] = 1
        start += 1
        q = deque()
        q.append([i,j])

        
        while q:
            if start > n:
                break
            x,y = q.popleft()
            
            if y==0 or y == w-1:
                d += 1
                if d >= 4:
                    d = 0
            di,dj = dirs[d]
            
            if w == 1:
                di,dj = -1,0
            ni,nj = x+di, y+dj

            if 0<=ni<rows and 0<=nj<w and visited[ni][nj] == 0 and maps[ni][nj] == 0:
                maps[ni][nj] = start
                start += 1
                q.append([ni,nj])

    tmp(rows)
    
    for i in range(0,rows):
        for j in range(w):
            if maps[i][j] == num:
                for k in range(i):
                    if maps[k][j] != 0:
                        answer += 1
        
    return answer+1