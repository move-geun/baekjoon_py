import sys
from collections import deque, Counter
N,M = map(int, sys.stdin.readline().split())
r,c,d = map(int, sys.stdin.readline().split())
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dists = [[-1,0],[0,1],[1,0],[0,-1]]

def clean(x,y,d):
    for n in range(4):
        nx = x + dists[(d+n)%4][0]
        ny = y + dists[(d+n)%4][1]

        if maps[nx][ny] == 0:
            return True
    return False

q = deque()
q.append([r,c,d])
maps[r][c] = 3

while q:
    i,j,d = q.popleft()
    if maps[i][j] == 0:
        maps[i][j] = 3

    if clean(i,j,d):
        for _ in range(4):
            d = (d+3)%4
            ni = i + dists[d][0]
            nj = j + dists[d][1]

            if maps[ni][nj] == 0:
                q.append([ni,nj,d])
                break
    else:
        ni = i + dists[d][0]*-1
        nj = j + dists[d][1]*-1

        if maps[ni][nj] == 1:
            break
        else:
            q.append([ni,nj,d])

cnt = 0
for map in maps:
    for m in map:
        if m == 3:
            cnt += 1
print(cnt)
