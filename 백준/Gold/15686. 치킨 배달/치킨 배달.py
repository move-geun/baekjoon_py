import sys
from itertools import combinations

input = sys.stdin.readline
n,m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

homes = []
store = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            homes.append([i+1, j+1])
        if maps[i][j] == 2:
            store.append([i+1, j+1])

dist = [[] for _ in range(len(homes))]

for i in range(len(homes)):
    for dx,dy in store:
        dist[i].append(abs(homes[i][0]-dx)+abs(homes[i][1]-dy))

min_dist = 10**18
S = len(store)
H = len(homes)

for comb in combinations(range(S), m):
    total_tmp = 0
    for h in range(H):
        tmp = min(dist[h][s] for s in comb)
        total_tmp += tmp

        if total_tmp >= min_dist:
            break
    else:
        min_dist = total_tmp

print(min_dist)