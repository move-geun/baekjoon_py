import sys

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split(' ')))
lst.sort()
total, tmp = 0,0
for i in lst:
    tmp += i
    total += tmp
print(total)