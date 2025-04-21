import sys
input = sys.stdin.readline
a,b = map(int, input().split())
def isPrime(n):
    if n<2:
        return False
    tmp = int(n**0.5)
    for i in range(2, tmp+1):
        if n%i==0:
            return False
    return True

for i in range(a, b+1):
    if isPrime(i):
        print(i)