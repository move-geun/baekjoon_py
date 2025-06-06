import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
ans = 0
max_cnt = -1

def bfs(i,j):
    visited[i][j] = 1
    q = deque()
    q.append([i,j])
    cnt = 1

    while q:
        x,y = q.popleft()
        for di, dj in dirs:
            ni,nj = x+di, y+dj

            if 0<=ni<n and 0<=nj<m and maps[ni][nj]==1 and visited[ni][nj] == 0:
                q.append([ni,nj])
                visited[ni][nj] = 1
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == 0:
            ans += 1
            tmp_cnt = bfs(i,j)
            if tmp_cnt >= max_cnt:
                max_cnt = tmp_cnt

print(ans)
print(max_cnt if max_cnt != -1 else 0)

