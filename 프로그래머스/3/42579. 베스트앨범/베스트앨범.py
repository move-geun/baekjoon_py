from collections import defaultdict

def solution(genres, plays):
    answer = []
    maps = defaultdict(lambda: [0, []])
    
    for i in range(len(genres)):
        maps[genres[i]][0] += plays[i]
        maps[genres[i]][1].append([plays[i], i])
        
    for genre, (total, lst) in maps.items():
        lst.sort(key=lambda x: x[0], reverse=True)
    
    tmp = list(maps.values())
    tmp.sort(reverse=True)

    for i in tmp:
        cnt = 0
        for j in range(min(len(i[1]),2)):
            answer.append(i[1][j][1])
    return answer