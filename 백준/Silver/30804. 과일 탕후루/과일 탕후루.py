import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

fruits = list(map(int, input().split()))

cnt = defaultdict(int)
distinct = 0            
si = 0
maxv = 0

for ei in range(n):
    if cnt[fruits[ei]] == 0:
        distinct += 1
    cnt[fruits[ei]] += 1

    while distinct > 2:
        cnt[fruits[si]] -= 1
        if cnt[fruits[si]] == 0:
            distinct -= 1
        si += 1

    length = ei - si + 1
    if length > maxv:
        maxv = length

print(maxv)