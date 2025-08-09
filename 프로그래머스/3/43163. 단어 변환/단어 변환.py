from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words.append(begin)
    visited = [0]*(len(words))
    
    def can(i,j):
        diff = sum(a!=b for a,b in zip(words[i], words[j]))
        return diff==1
    
    def bfs(idx):
        q = deque()
        q.append(idx)
        visited[idx] = 1
        
        while q:
            i = q.popleft()
            if words[i] == target:
                return visited[i]
            
            for j in range(len(words)):
                if visited[j] == 0 and can(i,j):
                    q.append(j)
                    visited[j] = visited[i]+1
    ans = bfs(len(words)-1)-1
    
    return ans if visited[words.index(target)] else 0 
    