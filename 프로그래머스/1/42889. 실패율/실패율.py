from collections import defaultdict

def solution(N, stages):
    answer = []
    maps = [0]*(N+2)
    
    for i in stages:
        maps[i] += 1
        
    total = len(stages)
    now = 0
    ans = []
    for i in range(1,len(maps)-1):
        if maps[i] == 0:
            ans.append([0, i])
        else:
            ans.append([maps[i]/(total-now), i])
        now += maps[i]
    ans.sort(key= lambda x: (-x[0], x[1]))
    
    return [x for i,x in ans]