import sys

N = int(sys.stdin.readline())
base = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
minus = plus = zero = 0

def sol(x,y,n):
    global minus, plus, zero
    check = base[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != base[i][j]:
                for k in range(3):
                    for l in range(3):
                        sol(x+k*n//3,y+l*n//3,n//3)
                return
    
    if check  == -1:
        minus += 1
    elif check == 0:
        zero += 1
    elif check == 1:
        plus += 1

sol(0,0,N)
print(minus)
print(zero)
print(plus)