import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

def bfs(start, target):
    visited = [False] * 10000
    parent  = [-1]    * 10000
    op      = ['']    * 10000

    q = deque([start])
    visited[start] = True

    while q:
        x = q.popleft()
        if x == target:
            break

        # D (Double)
        nx = (x * 2) % 10000
        if not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            op[nx]     = 'D'
            q.append(nx)

        # S (Subtract)
        nx = (x - 1) % 10000
        if not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            op[nx]     = 'S'
            q.append(nx)

        # L (Rotate left)
        nx = (x % 1000) * 10 + x // 1000
        if not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            op[nx]     = 'L'
            q.append(nx)

        # R (Rotate right)
        nx = (x % 10) * 1000 + x // 10
        if not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            op[nx]     = 'R'
            q.append(nx)

    # 경로 복원
    res = []
    cur = target
    while cur != start:
        res.append(op[cur])
        cur = parent[cur]
    return ''.join(reversed(res))

for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))


