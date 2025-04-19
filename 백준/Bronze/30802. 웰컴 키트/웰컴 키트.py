import math
n = int(input())
lst = list(map(int, input().split()))
t,p = map(int, input().split())

tmp = 0
for i in lst:
    tmp += math.ceil(i/t)
print(tmp)
print(f'{n//p} {n%p}')