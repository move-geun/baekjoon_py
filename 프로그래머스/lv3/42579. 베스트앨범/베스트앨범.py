from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_rank = defaultdict(int)
    rank = list()
    
    for i in range(len(genres)):
        genre_rank[genres[i]] += plays[i]
        plays[i] = (plays[i], genres[i], i)

    for i in sorted(genre_rank.items(), key = lambda item: item[1], reverse=True):
        rank.append(i[0])
    plays = sorted(plays, key=lambda play: (play[1], -play[0], play[2]))
    
    for i in rank:
        tmp = 0
        for j in plays:
            if tmp >= 2:
                break
            if i == j[1]:
                answer.append(j[2])
                tmp += 1
    
    return answer