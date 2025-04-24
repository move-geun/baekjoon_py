import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m,n,k = map(int, input().strip().split(' '))
    maps = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x,y = map(int, input().strip().split(' '))
        maps[y][x] = 1
    

    def bfs(j,i):
        maps[j][i] = 0
        q = deque([(j,i)])
        d = [[-1,0],[0,1],[1,0],[0,-1]]

        while q:
            y,x = q.popleft()

            for k in range(4):
                ny,nx = y+d[k][0], x+d[k][1]
                if 0<=nx<=m-1 and 0<=ny<=n-1 and maps[ny][nx] == 1:
                    q.append((ny,nx))
                    maps[ny][nx] = 0
        return True
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
