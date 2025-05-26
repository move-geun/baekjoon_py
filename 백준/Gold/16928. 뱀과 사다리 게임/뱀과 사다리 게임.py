import sys

from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split(' '))
visited = [-1]*101
move = {}
for i in range(n+m):
    st,et = map(int, input().split(' '))
    move[st] = et

q = deque()
q.append(1)
visited[1] = 0

while q:
    now = q.popleft()
    if now == 100:
        break

    for k in range(1,7):
        nxt = now + k

        if nxt > 100:
            continue

        if nxt in move:
            nxt = move[nxt]
        
        if visited[nxt] == -1:
            visited[nxt] = visited[now] + 1
            q.append(nxt)

print(visited[100])