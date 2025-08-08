from itertools import permutations

def solution(k, dungeons):
    answer = 0
    candi = list(permutations(dungeons, len(dungeons)))
    
    for can in candi:
        tk = k
        cnt = 0
        for sk, mk in can:
            if sk > tk:
                continue
            else:
                tk -= mk
                cnt += 1
        answer = max(cnt, answer)
    return answer