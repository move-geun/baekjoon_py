import sys
input = sys.stdin.readline
maps = [[] for _ in range(51)]

t = int(input())
for _ in range(t):
    a = input().strip()
    maps[len(a)].append(a)

for i in maps:
    if len(i):
        tmp = list(set(i))
        tmp.sort()
        for j in tmp:
            print(j)