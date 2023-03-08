# from collections import deque

# def bfs(start, end, maps):
# 	# 탐색할 방향
#     dy = [0, 1, -1, 0]
#     dx = [1, 0, 0, -1]
    
#     n = len(maps)       # 세로
#     m = len(maps[0])    # 가로
#     visited = [[False]*m for _ in range(n)]
#     que = deque()
#     flag = False
    
#     # 초깃값 설정
#     for i in range(n):
#         for j in range(m):
#         	# 출발하고자 하는 지점이라면 시작점의 좌표를 기록함
#             if maps[i][j] == start:      
#                 que.append((i, j, 0))    
#                 # 별도의 cost 리스트를 만들지 않고 que에 바로 기록(0)
#                 visited[i][j] = True
#                 flag = True; break 
#                 # 시작 지점은 한 개만 존재하기 때문에 찾으면 바로 나옴
#         if flag: break
                
#     # BFS 알고리즘 수행 (핵심)
#     while que:
#         y, x, cost = que.popleft()
        
#         if maps[y][x] == end:
#             return cost
        
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
            
#             # maps 범위내에서 벽이 아니라면 지나갈 수 있음
#             if 0<= ny <n and 0<= nx <m and maps[ny][nx] !='X':
#                 if not visited[ny][nx]:	# 아직 방문하지 않는 통로라면
#                     que.append((ny, nx, cost+1))
#                     visited[ny][nx] = True
                    
#     return -1	# 탈출할 수 없다면
        
            
# def solution(maps):
#     path1 = bfs('S', 'L', maps)	# 시작 지점 --> 레버
#     path2 = bfs('L', 'E', maps) # 레버 --> 출구
    
#     # 둘다 -1 이 아니라면 탈출할 수 있음
#     if path1 != -1 and path2 != -1:
#         return path1 + path2
        
#    	# 둘중 하나라도 -1 이면 탈출할 수 없음
#     return -1

from collections import deque

def bfs(maps):
    di,dj = [1,0,0,-1],[0,1,-1,0]
    row = len(maps[0])
    col = len(maps)
    visited = [[False]*row for _ in range(col)]
    flag = False
    q = deque()
    
    # 시작지점 찾아 q에 넣기
    for i in range(col):
        for j in range(row):
            if maps[i][j] == 'S':
                q.append((i,j,0))
                visited[i][j] = 1
                flag = True
                break
        if flag:
            break
    
    # bfs 돌기
    while q:
        i,j,cost = q.popleft()
        if maps[i][j] == 'E':
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
    answer = bfs(maps)
    if answer:
        return answer
    return -1

a = ["OOOOL","OOOOX","OOOOO","OXXXO","EXSXO"]
print(solution(a))