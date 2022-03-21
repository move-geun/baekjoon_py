from collections import deque


def bfs(list,a, visited):
    queue = deque()
    queue.append(a)
    visited[a] = 1

    while queue:
        v = queue.popleft()
        for i in list[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1



computer = int(input())
link = int(input())
base = [list() for _ in range(computer+1)]
for i in range(link):
    a,b = map(int,input().split())
    base[a].append(b)
    base[b].append(a)


visited = [0]*(computer+1)

for i in base:
    i.sort()

bfs(base,1,visited)

print(visited.count(1)-1)