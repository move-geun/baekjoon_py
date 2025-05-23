import sys

input = sys.stdin.readline
n,k = map(int, input().split(' '))
bag = [[0,0]]
for _ in range(n):
    w,v = map(int, input().split(' '))
    bag.append([w,v])

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w1 = bag[i][0]
        v1 = bag[i][1]

        if j < w1:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w1]+v1)

print(dp[n][k])