import sys

N = int(sys.stdin.readline())
base = list()
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    base.append([start,end])

base.sort(key= lambda x : (x[1],x[0]))

cnt = end = 0
for i,j in base:
    if i >= end:
        cnt += 1
        end = j
print(cnt)
