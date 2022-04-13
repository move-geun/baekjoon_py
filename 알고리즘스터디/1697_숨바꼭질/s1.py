from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 1
q = deque()
q.append(N)

while True:
    n = q.popleft()
    if n == K:
        ans = visited[n] - 1
        break
    for k in (n-1, n+1, n*2):
        if 0 <= k <= 100000 and visited[k] ==0:
            visited[k] = visited[n]+1
            q.append(k)
print(ans)
