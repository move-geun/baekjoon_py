from collections import deque

def solution(board):
    answer = 0
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    n,m = len(board), len(board[0])
    maps = [[9999999999]*m for _ in range(n)]
    q = deque()
        
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append([i,j,0])
                maps[i][j] = 0
        if q:
            break

    while q:
        pi,pj,c = q.popleft()
        
        if board[pi][pj] == 'G':
            return c

        for di,dj in dirs:
            ni,nj = pi,pj

            while 0<=ni+di<n and 0<=nj+dj<m and board[ni+di][nj+dj] != 'D':
                ni += di
                nj += dj
            
            if maps[ni][nj] > c+1:
                maps[ni][nj] = c+1
                q.append([ni,nj,c+1])
                   
    return -1