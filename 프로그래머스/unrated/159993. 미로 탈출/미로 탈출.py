from collections import deque

def bfs(s,e,maps):
    di,dj = [1,0,0,-1],[0,1,-1,0]
    row = len(maps[0])
    col = len(maps)
    visited = [[False]*row for _ in range(col)]
    flag = False
    q = deque()
    
    # 시작지점 찾아 q에 넣기
    for i in range(col):
        for j in range(row):
            if maps[i][j] == s:
                q.append((i,j,0))
                visited[i][j] = 1
                flag = True
                break
        if flag:
            break
    
    # bfs 돌기
    while q:
        i,j,cost = q.popleft()
        if maps[i][j] == e:
            return cost
        
        for t in range(4):
            ni = i + di[t]
            nj = j + dj[t]
            
            if 0<=ni<col and 0<=nj<row and maps[ni][nj] != 'X':
                if not visited[ni][nj]:
                    q.append((ni,nj,cost+1))
                    visited[ni][nj] = 1
                    
    return -1

def solution(maps):
    answer1 = bfs('S','L',maps)
    answer2 = bfs('L','E',maps)
    if answer1 != -1 and answer2 != -1:
        return answer1 +answer2
    return -1