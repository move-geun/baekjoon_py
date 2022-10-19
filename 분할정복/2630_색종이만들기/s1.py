
def blue(row,col,lst):
    for i in range(row):
        for j in range(col):
            if lst[i][j] != 1:
                return False
    return True


def white(row,col,lst):
    for i in range(row):
        for j in range(col):
            if lst[i][j] != 0:
                return False
    return True

def divide(i, j, lst):
    global blue_count, white_count
    if blue(i,j,lst):
        blue_count+= 1
    elif white(i,j,lst):
        white_count += 1
    elif blue(i,j,lst) == False or white(i,j,lst) == False:
        divide(i,j//2,lst)
        divide(j//2,j,lst)

import sys
N = int(sys.stdin.readline())
base = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
blue_count = white_count = 0
divide(N,N,base)
print(white_count)
print(blue_count)