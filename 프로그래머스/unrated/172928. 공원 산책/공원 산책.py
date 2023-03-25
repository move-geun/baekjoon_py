def solution(park, routes):
    answer = []
    direction = {"E":(0,1),"W":(0,-1),"N":(-1,0),"S":(1,0)}
    for i in range(0,len(park)):
        for j in range(0, len(park[i])):
            if park[i][j] == "S":
                start = (i,j)
    
    for i in range(0,len(routes)):
        di,dis = routes[i].split(" ")
        cango = True
        for j in range(1,int(dis)+1):
            ni,nj = start[0] + direction[di][0]*j, start[1] + direction[di][1]*j
            if 0 <= ni < len(park) and 0 <= nj < len(park[0]) and park[ni][nj] != "X":
                cango = True
            else:
                cango = False
                break
        
        if cango:
            start = (start[0] + direction[di][0]*int(dis), start[1] + direction[di][1]*int(dis))
    
    answer.append(start[0])
    answer.append(start[1])
    return answer