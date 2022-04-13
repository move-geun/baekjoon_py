import copy
# 벽 세우고
# 바이러스 돌리고
# 안전가옥 세기

def wall(cnt):
    global max_safe
    # 종료조건
    if cnt == 3:
        visited = copy.deepcopy(base)
        for i in range(N):
            for j in range(M):
                if base[i][j] == 2:
                    virus(i, j, visited)

        # 0 세기
        cnt = 0
        for i in visited:
            cnt += i.count(0)

        max_safe = max(max_safe, cnt)
        return

    # 도는조건
    for i in range(N):
        for j in range(M):
            if base[i][j] == 0:
                base[i][j] = 1
                wall(cnt+1)
                base[i][j] = 0


def virus(i, j, lst):
    pos = [[1,0],[-1,0],[0,1],[0,-1]]
    for di, dj in pos:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < N:
            if lst[ni][nj]==0:
                lst[ni][nj] = 2
                virus(ni, nj, lst)
    return


N, M = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(N)]
max_safe = -1
wall(0)
print(max_safe)
