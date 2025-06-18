import sys

input = sys.stdin.readline

n = int(input())
maps = [[int(input())]]
for _ in range(n-1):
    tmp = list(map(int, input().split()))
    maps.append(tmp)

dist = [-1,0]

for i in range(1, n):
    for j in range(len(maps[i])):
        candi = []
        for d in dist:
            nj = j+d

            if 0<=nj<len(maps[i-1]):
                candi.append(maps[i-1][nj])
        maps[i][j] += max(candi)

print(max(maps[-1]))