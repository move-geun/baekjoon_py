import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split(' '))
parents = list(range(n+1))

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parents[rb] = ra
    
for _ in range(m):
    sn, en = map(int, input().split(' '))
    union(sn,en)

for i in range(1,n+1):
    find(i)

print(len(set(parents[1:])))