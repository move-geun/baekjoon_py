import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst = list(set(lst))
lst.sort()
ans = []

def dfs(num, cnt):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(lst.index(num),len(lst)):
        ans.append(lst[i])
        dfs(lst[i], cnt+1)
        ans.pop()

dfs(lst[0],0)