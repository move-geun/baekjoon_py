import sys

input = sys.stdin.readline
n,k = map(int, input().split())

tmp = 1
tmp2 = 1
tmp3 = 1

for i in range(1,n+1):
    tmp *= i

for i in range(1, n-k+1):
    tmp2 *= i

for i in range(1,k+1):
    tmp3 *= i

print(tmp//(tmp2*tmp3)%10007)