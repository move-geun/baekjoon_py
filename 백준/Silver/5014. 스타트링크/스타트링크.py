import sys
from collections import deque

input = sys.stdin.readline
f,s,g,u,d = map(int, input().split())
visited = [0]*(f+1)

def bfs(i,cnt):
    q = deque()
    q.append([i,cnt])
    visited[i] = 1

    while q:
        x,val = q.popleft()
        if x == g:
            return val
        
        for di in [u, d*-1]:
            nx = x+di

            if 1<=nx<=f and visited[nx]==0:
                q.append([nx, val+1])
                visited[nx] = 1
    return -1

tmp = bfs(s,0)
print(tmp if tmp!= -1 else 'use the stairs')