
# 벽 세우고, 바이러스 퍼트리기
def dfs(cnt, depth, candi):
    if depth == 3:
        virus(base)
        return
    for i in range(cnt, len(candi)):
        base[candi[i][0]][candi[i][1]] = 1
        dfs(cnt+1, depth+1, candi)
        base[candi[i][0]][candi[i][1]] = 0


def virus(base):
    global min_virus
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = list()
    virus_cnt = 0

    for i, j in start:
        visited[i][j] = 2
        virus_cnt += 1
        q.append((i,j))

    while q:
        i, j = q.pop(0)

        if min_virus <= virus_cnt:
            break

        for di, dj in pos:
            ni = i + di
            nj = j + dj
            if 0 <= ni < M and 0 <= nj < N and base[ni][nj]==0 and visited[ni][nj]!=2:
                q.append((ni,nj))
                visited[ni][nj] = 2
                virus_cnt += 1

    if virus_cnt < min_virus:
        min_virus = virus_cnt
    return



N, M  = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(N)]
wall_candi = list()
wall_cnt = 0
min_virus = 1000000
start = list()

# 바이러스 시작점 찾기
# 벽 후보 찾기
for i in range(N):
    for j in range(M):
        if base[i][j] == 0:
            wall_candi.append((i, j))
        elif base[i][j] == 2:
            start.append((i, j))
        elif base[i][j] == 1:
            wall_cnt += 1

pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]

dfs(0, 0, wall_candi)

print(N*M - wall_cnt -3 - min_virus)

