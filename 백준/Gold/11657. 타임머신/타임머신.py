import sys

input = sys.stdin.readline
INF = 1e9
n,m = map(int, input().split())
graph = []
dist = [INF]*(n+1)   
for _ in range(m):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

def bellman(num):

    dist[num] = 0

    for i in range(n):
        for j in range(m):
            a,b,c = graph[j]

            if dist[a] != INF and dist[b] > dist[a]+c:
                dist[b] = dist[a]+c

                if i == n-1:
                    return True
    return False

minus = bellman(1)

if minus:
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])

