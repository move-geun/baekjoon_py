import sys
input = sys.stdin.readline

t = int(input())
def calcu(t):
    for i in range(t//5,-1,-1):
        tmp = t-i*5
        if tmp%3 == 0:
            return (i + tmp//3)
    return -1

print(calcu(t))
