import sys

input = sys.stdin.readline
r,c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]
dist = [[1,0],[-1,0],[0,1],[0,-1]]
visited = [0]*26
ans = -1


def dfs(x,y,cnt):
    global ans
    if cnt > ans:
        ans = cnt
    
    for di,dj in dist:
        ni,nj = x+di, y+dj

        if 0<=ni<r and 0<=nj<c and visited[ord(maps[ni][nj])-65] == 0:
            visited[ord(maps[ni][nj])-65] = 1
            dfs(ni,nj,cnt+1)
            visited[ord(maps[ni][nj])-65] = 0


visited[ord(maps[0][0])-65] = 1
dfs(0,0,1)

print(ans)