import sys
input = sys.stdin.readline

n = int(input())
lsts = list(map(int, input().split()))
x = int(input())

lsts.sort()
si, ei = 0, n-1
cnt = 0

while si < ei:
    s = lsts[si] + lsts[ei]
    if s == x:
        cnt += 1
        si += 1
        ei -= 1
    elif s < x:
        si += 1
    else:  # s > x
        ei -= 1

print(cnt)
