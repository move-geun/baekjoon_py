import sys
input = sys.stdin.readline

t = int(input()) 
lst = [int(input()) for _ in range(t)]
dp = [0]*(max(lst)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, max(lst)+1):
    dp[i] = sum(dp[i-3:i])

for i in lst:
    print(dp[i])
