import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 1e9
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    st,et,v = map(int, input().split())
    graph[st][et] = min(graph[st][et],v)


for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    ans = []
    for j in range(1, n+1):
        if graph[i][j] == INF:
            ans.append(0)
        else:
            ans.append(graph[i][j])
    print(*ans)
