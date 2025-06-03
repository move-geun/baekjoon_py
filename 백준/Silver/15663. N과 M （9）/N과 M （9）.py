import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

visited = [False] * n
res = [0] * m

def dfs(depth):
    if depth == m:
        print(*res)
        return

    used = set()  
    for i in range(n):
        if not visited[i] and lst[i] not in used:
            used.add(lst[i])
            visited[i] = True
            res[depth] = lst[i]
            dfs(depth + 1)
            visited[i] = False

dfs(0)
