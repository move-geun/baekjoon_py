import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
maxh = max(max(row) for row in grid)

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
ans = 1  

for H in range(1, maxh):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] > H:
                cnt += 1
                dq = deque([(i,j)])
                visited[i][j] = True
                while dq:
                    x,y = dq.popleft()
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and grid[nx][ny] > H:
                                visited[nx][ny] = True
                                dq.append((nx,ny))
    ans = max(ans, cnt)
print(ans)