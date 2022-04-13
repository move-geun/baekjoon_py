# 시간초과..

import copy
from collections import deque

# 벽 3개 쌓은 리스트를 만들고
# 바이러스를 모두 퍼트리고
# 안전가옥 숫자 세기

# 벽 세우기
def dfs(depth):
    # 벽을 3개 세우면, virus를 퍼트려보자
    if depth == 3:
        virus()
        return

    # 하나씩 돌면서 0이면 벽 세우자
    for i in range(N):
        for j in range(M):
            if base[i][j] == 0:
                base[i][j] = 1
                dfs(depth+1)
                base[i][j] = 0


# 바이러스 퍼트리고 숫자세기
def virus():
    global max_safe, min_vcnt
    temp_base = copy.deepcopy(base)
    vpoint = deque()
    vcnt = 0

    for i in range(N):
        for j in range(M):
            if base[i][j] == 2:
                vpoint.append([i,j])

    while vpoint:
        i, j = vpoint.popleft()
        
        for di,dj in pos:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < M and temp_base[ni][nj] == 0:
                temp_base[ni][nj] = 2
                vcnt += 1
                vpoint.append([ni,nj])
        if min_vcnt <= vcnt:
            return

    cnt = 0
    for i in range(N):
        cnt += temp_base[i].count(0)

    if max_safe < cnt:
        max_safe = cnt


N, M = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(N)]
max_safe = -1
min_vcnt = 1000
pos = [[1,0],[-1,0],[0,1],[0,-1]]
dfs(0)
print(max_safe)



