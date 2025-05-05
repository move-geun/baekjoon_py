
def dfs(i,j,depth,value):
    global max_value

    # 종료조건
    if depth == 3:
        if max_value < value:
            max_value = value
        return
        
    # 도는조건
    pos = [[1,0],[-1,0],[0,1],[0,-1]]
    for di,dj in pos:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]==0:
            visited[ni][nj] = 1
            dfs(ni, nj, depth+1, value + base[ni][nj])
            visited[ni][nj] = 0




def fuck(i,j,value,ffpos):
    global max_value

    for di,dj in ffpos:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M:
            value += base[ni][nj]
    
    if max_value < value:
        max_value = value


N, M = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
max_value = -1
f_pos = [[[0,1],[0,2],[1,1]],
         [[0,1],[0,2],[-1,1]],
         [[1,0],[2,0],[1,1]],
         [[1,0],[1,-1],[2,0]]]

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i,j,0,base[i][j])
        visited[i][j] = 0
        for ff_pos in f_pos:
            fuck(i,j,base[i][j],ff_pos)

print(max_value)
        

