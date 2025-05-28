import sys

input = sys.stdin.readline
n,m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
lst.sort()
ans = []

def dfs(i):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for j in range(n):
        if lst[j] not in ans:
            ans.append(lst[j])
            dfs(j+1)
            ans.pop()

dfs(0)