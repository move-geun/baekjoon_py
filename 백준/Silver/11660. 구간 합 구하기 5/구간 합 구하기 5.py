import sys
input = sys.stdin.readline

n,m = map(int, input().split(' '))
maps = []

for i in range(n):
    tmp = list(map(int, input().split()))
    j = 1
    while j<len(tmp):
        tmp[j] += tmp[j-1]
        j += 1
    
    maps.append(tmp)

for _ in range(m):
    x1,y1,x2,y2 = map(lambda v: int(v)-1, input().split())

    tmp = 0
    for i in range(x1,x2+1):
        if (y1-1) >= 0:
            tmp += maps[i][y2]-maps[i][y1-1]
        else:
            tmp += maps[i][y2]
    print(tmp)
