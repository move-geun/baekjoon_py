import sys

N = int(sys.stdin.readline())


for i in range(1, N+1):
    tmp = i
    for j in str(i):
        tmp += int(j)
    if tmp == N:
        print(i)
        break
    if i == N and tmp != N:
        print(0)