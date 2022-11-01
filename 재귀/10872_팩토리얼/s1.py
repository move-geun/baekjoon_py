import sys


def sol(a):
    result = 1
    if a > 0 :
        result = a * sol(a-1)
    return result

N = int(sys.stdin.readline())
print(sol(N))
