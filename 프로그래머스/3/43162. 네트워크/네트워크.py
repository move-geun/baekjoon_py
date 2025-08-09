from collections import deque

def solution(n, computers):
    visited = [0]*(n)
    ans = 0
    
    def bfs(i):
        q = deque()
        
        for j in range(n):
            if j == i:
                continue
            else:
                if computers[i][j] and visited[j] == 0:
                    q.append(j)
                    visited[j] = 1
        
        while q:
            w = q.popleft()
            
            for k in range(n):
                if computers[w][k] == 1 and visited[k] ==0 :
                    q.append(k)
                    visited[k] = 1
    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            ans += 1
        
    return ans
