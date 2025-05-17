import sys

input = sys.stdin.readline
n, x = map(int, input().split(' '))
days = list(map(int, input().split(' ')))
cnt = 1
window = sum(days[:x])
maxV = window
for i in range(x,n):
    window = window - days[i-x] + days[i]
    if maxV == window:
        cnt += 1
    elif maxV < window:
        cnt = 1
        maxV = window

if maxV != 0:
    print(maxV)
    print(cnt)
else:
    print('SAD')
