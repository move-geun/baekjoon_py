import sys

input = sys.stdin.readline

t = int(input())
maps = list(list(map(int, input().split(' '))) for _ in range(t))
answer = [0,0]

def divide(x,y,n):
    color = maps[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if maps[i][j] != color:
                m = n//2
                divide(x,y,m)
                divide(x, y+m, m)
                divide(x+m, y, m)
                divide(x+m,y+m,m)
                return
    
    if color:
        answer[1] += 1
    else:
        answer[0] += 1

divide(0,0,t)
print(answer[0])
print(answer[1])