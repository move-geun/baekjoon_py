import sys
from collections import deque

input = sys.stdin.readline
dirs = [[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]

t = int(input())
for _ in range(t):
    n = int(input())
    start = list(map(int, input().split(' ')))
    end = list(map(int, input().split(' ')))
    maps = [[0]*n for _ in range(n)]

    if start == end:
        print(0)
        continue

    q = deque()
    q.append(start)
    maps[start[0]][start[1]] = 1

    while q:
        x,y = q.popleft()
        for di,dj in dirs:
            ni,nj = x+di, y+dj

            if 0<=ni<n and 0<=nj<n and maps[ni][nj] == 0:
                maps[ni][nj] = maps[x][y] + 1
                if ni==end[0] and nj==end[1]:
                    print(maps[ni][nj]-1)
                    q.clear()
                    break
                q.append([ni,nj])
        else:
            continue
        break