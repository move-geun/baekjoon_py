from collections import deque

def bfs(base, i, visit):
    queue = deque([i])
    visit[i] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in base[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


def dfs(base, v, visit):
    visit[v] = True
    print(v, end=' ')
    for i in base[v]:
        if not visit[i]:
            dfs(base,i,visit)

n,m,v = map(int, input().split())
base = [list() for _ in range(n+1)]
for a in range(m):
    first, end = map(int, input().split())
    base[first].append(end)
    base[end].append(first)

for b in base:
    b.sort()

visit = [False]*(n+1)
dfs(base,v,visit)
print()
visit = [False]*(n+1)
bfs(base,v,visit)
