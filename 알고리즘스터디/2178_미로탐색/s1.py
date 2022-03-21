from collections import deque

def bfs(list,x,y):
    queue = deque()
    queue.append((x,y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and base[nx][ny] == 1:
                base[nx][ny] = base[x][y]+1
                queue.append((nx,ny))
    return base[n-1][m-1]



n,m = map(int,input().split())
base = list()
for _ in range(n):
    base.append(list(map(int,list(input()))))

print(bfs(base,0,0))

