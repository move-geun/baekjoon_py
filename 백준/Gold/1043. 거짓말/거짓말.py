import sys
from collections import deque

input = sys.stdin.readline


n,m = map(int, input().split())
known_lst = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
party = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    party.append(tmp[1:])
    for i in range(1,tmp[0]+1):
        for j in range(1,tmp[0]+1):
            if i == j:
                continue
            graph[tmp[i]].append(tmp[j])

if known_lst[0] == 0:
    print(m)
else:
    q = deque()
    for i in known_lst[1:]:
        q.append(i)
    
    while q:
        x = q.popleft()
        visited[x] = 1

        for j in graph[x]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)
    
    cnt = 0
    for i in party:
        flag = True
        for j in i:
            if visited[j] == 1:
                flag = False
        cnt += 1 if flag else 0
    print(cnt)

