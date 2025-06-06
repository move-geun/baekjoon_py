import sys
from collections import deque

input = sys.stdin.readline
r,c = map(int, input().split(' '))
maps = list(list(input().strip()) for _ in range(r))
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
v_j = [[0]*(c) for _ in range(r)]
v_f = [[0]*(c) for _ in range(r)]
q_j = deque()
q_f = deque()

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'J':
            q_j.append([i,j])
            v_j[i][j] = 1
        elif maps[i][j] == 'F':
            q_f.append([i,j])
            v_f[i][j] = 1

def bfs():
    while q_f:
        x,y = q_f.popleft()

        for di,dj in dirs:
            ni,nj = x+di, y+dj

            if 0<=ni<r and 0<=nj<c and v_f[ni][nj]==0 and maps[ni][nj] != '#':
                q_f.append([ni,nj])
                v_f[ni][nj] = v_f[x][y] + 1
    
    while q_j:
        x,y = q_j.popleft()
        
        for di,dj in dirs:
            ni,nj = x+di, y+dj

            if 0<=ni<r and 0<=nj<c:
                if v_j[ni][nj] == 0 and maps[ni][nj] != '#' and (v_f[ni][nj] == 0 or v_f[ni][nj] > v_j[x][y]+1):
                    q_j.append([ni,nj])
                    v_j[ni][nj] = v_j[x][y] + 1
            
            else:
                return print(v_j[x][y])
    return print('IMPOSSIBLE')

bfs()
