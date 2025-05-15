import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split(' ')))

kinds = 0
maxv = 0
fruits = defaultdict(int)
si = 0

for ei in range(n):
    if fruits[lst[ei]] == 0:
        kinds += 1
    fruits[lst[ei]] += 1

    while kinds > 2:
        fruits[lst[si]] -= 1
        if fruits[lst[si]] == 0:
            kinds -= 1
        si += 1
    
    maxv = max(maxv, ei-si+1)

print(maxv)