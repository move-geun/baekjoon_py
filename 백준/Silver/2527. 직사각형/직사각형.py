import sys

input = sys.stdin.readline

for i in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if (x2 < x3) or (x4 < x1) or (y3 > y2) or (y1 > y4):
        print('d')
        continue
    
    if (x2 == x3 and y2 == y3) or (x2 == x3 and y1 == y4) or (x1 == x4 and y1 == y4) or (x1 == x4 and y2 == y3):
        print('c')
        continue

    if x3 == x2 or x1 == x4 or y1 == y4 or y2 == y3:
        print('b')
        continue

    else:
        print('a')
        continue
