import sys
input = sys.stdin.readline

t = int(input()) 
lst = [int(input()) for _ in range(t)]
lst.insert(0,0)
dp = [0]*(t+1)
if t <=2:
    print(sum(lst[::]))
else:
    dp[1] = lst[1]
    dp[2] = lst[1]+lst[2]

    for i in range(3,t+1):
        dp[i] = max(dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i])

    print(dp[-1])