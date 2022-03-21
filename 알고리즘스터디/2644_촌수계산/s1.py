import sys
sys.stdin = open('input.txt','r')
from collections import deque


def bfs(base,t1):
    queue = deque()
    queue.append(t1)

    while queue:
        r = queue.popleft()

        for i in base[r]:
            if visited[i] == 0:
                visited[i] = visited[r] + 1
                queue.append(i)
    return -1

# 전체 인원
n = int(input())
# target1, target2
t1, t2 = map(int,input().split())
#연결 족보 base
base = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
tc =int(input())
for _ in range(tc):
    x,y = map(int,input().split())
    base[x].append(y)
    base[y].append(x)

bfs(base,t1)

if visited[t2]>0:
    print(visited[t2])
else:
    print(-1)
