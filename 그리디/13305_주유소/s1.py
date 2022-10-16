import sys

N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
min_cost = cost[0]
aws = 0
for i in range(N-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    aws += min_cost * dist[i]

print(aws)


