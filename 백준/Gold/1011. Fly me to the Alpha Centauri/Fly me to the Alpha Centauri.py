from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x 
    tmp = 0 
    cnt = 0 
    moving = 0 

    while tmp < distance:
        cnt += 1
        if cnt % 2 != 0:
            moving += 1
        tmp += moving
    print(cnt)
