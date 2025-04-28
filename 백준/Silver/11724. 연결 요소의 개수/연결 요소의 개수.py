import sys

input = sys.stdin.readline
n,m = map(int, input().split(' '))
visited = [0]*(n+1)
maps = [[] for _ in range(n+1)]
for _ in range(m):
    st,et = map(int, input().split(' '))
    maps[st].append(et)
    maps[et].append(st)

cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        cnt += 1
        visited[i] = 1
        nexts = maps[i]
        while nexts:
            next = nexts.pop()
            if visited[next] == 0:
                visited[next] = 1
                items = maps[next]
                for item in items:
                    if item not in nexts : nexts.append(item)

print(cnt)