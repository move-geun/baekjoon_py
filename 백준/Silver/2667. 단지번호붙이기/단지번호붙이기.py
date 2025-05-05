from collections import deque

N = int(input())
base = list()
visited = [[0]*N for _ in range(N)]
for _ in range(N):
    base.append(list(map(int,input())))


pos = [[1,0],[-1,0],[0,1],[0,-1]]

flag = 0

def bfs(x,y):
    global flag
    queue = deque()
    queue.append([x,y])

    flag += 1
    visited[x][y]= flag

    while queue:
        i,j = queue.popleft()
        if base[i][j] == 1:
            visited[i][j] = flag
            for di, dj in pos:
                ni = di+i
                nj = dj+j
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and base[ni][nj] == 1:
                    queue.append([ni,nj])
                    visited[ni][nj] = flag



for i in range(N):
    for j in range(N):
        if base[i][j] == 1 and visited[i][j] ==0:
            bfs(i,j)

print(flag)
results = list()
for num in range(1,flag+1):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == num:
                cnt += 1
    results.append(cnt)

results.sort()

for i in results:
    print(i)
