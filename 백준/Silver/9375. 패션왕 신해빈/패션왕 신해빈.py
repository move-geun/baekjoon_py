import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input()) 
for _ in range(t):
    tmp = int(input())
    cnt = 1
    cloth = defaultdict(int)
    for _ in range(tmp):
        a,b = map(str, input().strip().split())
        cloth[b] += 1
    lst = list(cloth.values())
    for i in lst:
        cnt *= i+1

    print(cnt-1)