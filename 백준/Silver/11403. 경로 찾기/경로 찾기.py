import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
answer = [[0]*n for _ in range(n)]
maps = [list(map(int, input().split(' '))) for _ in range(n)]

def bfs(x):
    q = deque()
    q.append(x)
    visited = [0]*(n)

    while q:
        tmp = q.popleft()

        for j in range(n):
            if visited[j]==0 and maps[tmp][j]:
                answer[x][j] = 1
                q.append(j)
                visited[j] = 1

for i in range(n):
    bfs(i)

for a in answer:
    print(*a)