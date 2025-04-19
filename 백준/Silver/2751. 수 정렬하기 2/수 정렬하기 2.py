import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    tmp = int(input())
    lst.append(tmp)
lst.sort()
for i in lst:
    print(i)