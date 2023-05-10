def solution(players, callings):
    rank = {}
    names = {}
    for i in range(len(players)):
        rank[i] = players[i]
        names[players[i]] = i
    
    for i in callings:
        pre = names[i]
        rank[pre], rank[pre-1] = rank[pre-1], i
        names[rank[pre]] += 1
        names[rank[pre-1]] -= 1
    players = list(rank.values())
        
    return players