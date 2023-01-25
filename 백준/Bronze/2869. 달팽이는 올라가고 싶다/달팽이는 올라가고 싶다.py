import sys

A,B,V = map(int, sys.stdin.readline().split())
h = V - A
if h % (A-B) == 0:
    day = int(h/(A-B))
else:
    day = int(h/(A-B) + 1)
print(day + 1)