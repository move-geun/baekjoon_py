import sys

INF = 1e9
input = sys.stdin.readline
t = int(input())
def bell(n, dist, edge):
    dist[n] = 0

    for i in range(n):
        for st,et,va in edge:
            if dist[et] > dist[st]+va:
            # if dist[st] != INF and dist[et] > dist[st]+va:
                dist[et] = dist[st]+va

                if i == n-1:
                    return True
    return False

for _ in range(t):
    n,m,w = map(int, input().split())
    dist = [INF]*(n+1)
    edge = []
    for _ in range(m):
        st,et,va = map(int, input().split())
        edge.append([st,et,va])
        edge.append([et,st,va])
    
    for _ in range(w):
        st,et,va = map(int, input().split())
        edge.append([st,et,-va])
    
    ans = bell(n, dist, edge)

    print('YES' if ans else 'NO')