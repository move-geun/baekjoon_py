import sys

input = sys.stdin.readline
n,s = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

def dfs(idx, tmp_sum):
    global cnt

    if idx==n:
        if tmp_sum == s:
            cnt += 1
        return
    
    dfs(idx+1, tmp_sum + lst[idx])
    dfs(idx+1, tmp_sum)

dfs(0,0)

if s==0:
    cnt -= 1

print(cnt)

