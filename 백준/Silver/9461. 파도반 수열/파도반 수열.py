import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input()) 
maps = [0,1,1,1,2,2]
for i in range(6, 101):
    maps.append(maps[i-5] + maps[i-1])
for _ in range(t):
    tmp = int(input())
    print(maps[tmp])