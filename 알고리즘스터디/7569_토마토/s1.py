from collections import deque

M, N, H = map(int, input().split())
base = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
pos = [[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]
ans = 0
max_value = 0

q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if base[h][n][m] == 1:
                q.append([h, n, m])

while q:
    h, n, m = q.popleft()
    for dh, dn, dm in pos:
        nh = h + dh
        nn = n + dn
        nm = m + dm

        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and base[nh][nn][nm] == 0:
            base[nh][nn][nm] = base[h][n][m] + 1
            q.append([nh, nn, nm])

for h in base:
    for n in h:
        for m in n:
            if max_value < m:
                max_value = m
            if m == 0:
                ans = -1

if ans == -1:
    print(ans)
else:
    print(max_value-1)

