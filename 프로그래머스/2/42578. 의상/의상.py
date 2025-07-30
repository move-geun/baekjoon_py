from collections import defaultdict

def solution(clothes):
    answer = 1
    maps = defaultdict(int)
    for cloth, kind in clothes:
        maps[kind] += 1
    
    val = list(maps.values())

    for i in val:
        answer *= (i+1)
    
    return answer - 1