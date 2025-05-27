import sys

input = sys.stdin.readline
n,m = map(int, input().split(' '))
ans = []

def dfs(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(start, n+1):
        if i not in ans:
            ans.append(i)
            dfs(i+1)
            ans.pop()

dfs(1)