import sys

def fibo(a):
    result = 0
    if a == 0:
        return 0
    if a == 1 :
        return 1
    else:
        result = fibo(a-1) + fibo(a-2)
    return result
    

N = int(sys.stdin.readline())
print(fibo(N))