import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
lst = [int(x) for x in input().split()]
dist = [] 

if k >= n:
    print(0)
    exit()

lst.sort() 
for i in range(1, n):
    dist.append(lst[i] - lst[i - 1])

for _ in range(k - 1):
    dist[dist.index(max(dist))] = 0

print(sum(dist))