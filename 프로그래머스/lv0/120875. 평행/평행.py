def solution(dots):
    answer = 0
    candi = [[0,1,2,3],[0,2,1,3],[0,3,1,2]]
    
    for can in candi:
        if (dots[can[1]][1] - dots[can[0]][1]) /(dots[can[1]][0] - dots[can[0]][0]) == (dots[can[3]][1] - dots[can[2]][1]) /(dots[can[3]][0] - dots[can[2]][0]):
            answer = 1
            break
    
    return answer