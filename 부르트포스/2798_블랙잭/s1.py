import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
base = list(map(int, sys.stdin.readline().split()))

aws = 0
for i in combinations(base,3):
    if sum(i) <= M and (M-sum(i) < M-aws):
        aws = sum(i)

print(aws)