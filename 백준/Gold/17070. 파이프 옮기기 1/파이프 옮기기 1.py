import sys

input = sys.stdin.readline
n = int(input())
visited = [[0]*(n) for _ in range(n)]
maps = [list(map(int, input().split())) for _ in range(n)]
visited[0][0] = 1
visited[0][1] = 1
cnt = 0

def find(i,j,t):
    global cnt
    if i==n-1 and j==n-1:
        cnt += 1
        return
    
    if t == 0:
        if 0<=i<n and 0<=j+1<n and maps[i][j+1] == 0 and visited[i][j+1] == 0:
            find(i,j+1,0)
        if 0<=i+1<n and 0<=j+1<n and maps[i+1][j+1] == 0 and maps[i][j+1] ==0 and maps[i+1][j]==0 and visited[i+1][j+1] ==0:
            find(i+1,j+1,2)
    
    elif t==1:
        if 0<=i+1<n and 0<=j<n and maps[i+1][j] == 0 and visited[i+1][j] == 0:
            find(i+1,j,1)
        if 0<=i+1<n and 0<=j+1<n and maps[i+1][j+1] == 0 and maps[i][j+1] ==0 and maps[i+1][j]==0 and visited[i+1][j+1] ==0:
            find(i+1,j+1,2)
    
    elif t==2:
        if 0<=i<n and 0<=j+1<n and maps[i][j+1] == 0 and visited[i][j+1] == 0:
            find(i,j+1,0)
        if 0<=i+1<n and 0<=j<n and maps[i+1][j] == 0 and visited[i+1][j] == 0:
            find(i+1,j,1)
        if 0<=i+1<n and 0<=j+1<n and maps[i+1][j+1] == 0 and maps[i][j+1] ==0 and maps[i+1][j]==0 and visited[i+1][j+1] ==0:
            find(i+1,j+1,2)

find(0,1,0)

print(cnt)