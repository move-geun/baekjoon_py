import sys
input = sys.stdin.readline

m, n = map(int, input().split())
maps = dict()
for _ in range(m):
    link, pw = map(str, input().strip().split(' '))
    maps[link] = pw
for _ in range(n):
    link = input().strip()
    print(maps[link])