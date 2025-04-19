import sys
input = sys.stdin.readline

maps = [0]*100001
t = int(input())
for _ in range(t):
    a = int(input())
    maps[a] += 1

for i in range(len(maps)):
    if maps[i] != 0:
        for k in range(maps[i]):
            print(i)
