import sys
import heapq

input = sys.stdin.readline
INF = 10**9
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
case = 1

while True:
    n = int(input().strip())
    if n == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF]*n for _ in range(n)]
    dist[0][0] = grid[0][0]
    pq = [(dist[0][0], 0, 0)]

    while pq:
        val, i, j = heapq.heappop(pq)

        if val > dist[i][j]:
            continue

        for dx, dy in dirs:
            ni, nj = i+dx, j+dy
            if 0 <= ni < n and 0 <= nj < n:
                nd = val + grid[ni][nj]
                if nd < dist[ni][nj]:
                    dist[ni][nj] = nd
                    heapq.heappush(pq, (nd, ni, nj))

    print(f"Problem {case}: {dist[n-1][n-1]}")
    case += 1
