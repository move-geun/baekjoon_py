from collections import deque

def bfs(i, visited, graph):
    ans = 1
    visited[i] = 1
    q = deque()
    q.append(i)
    while q:
        next = q.popleft()
        for ti in graph[next]:
            if visited[ti] == 0:
                q.append(ti)
                visited[ti] = 1
                ans += 1
    return ans
        

def solution(n, wires):
    res = []
    graph = [[] for _ in range(n+1)]
    
    for si,ei in wires:
        graph[si].append(ei)
        graph[ei].append(si)
    
    for ti,tj in wires:
        graph[ti].remove(tj)
        graph[tj].remove(ti)
        visited = [0]*(n+1)
        
        ans = []
        for i in range(1, n+1):
            if visited[i] == 0:
                ans.append(bfs(i,visited,graph))
        res.append(abs(ans[0]-ans[1]))
        graph[ti].append(tj)
        graph[tj].append(ti)
    
    return min(res)
