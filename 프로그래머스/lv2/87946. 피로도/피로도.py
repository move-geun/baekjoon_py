from itertools import permutations

def solution(k, dungeons):
    answer = []
    tmp_k = k
    candi = list(permutations([i for i in range(len(dungeons))],len(dungeons)))
    for can in candi:
        tmp = 0
        tmp_k = k
        for i in can:
            if tmp_k >= dungeons[i][0]:
                tmp_k -= dungeons[i][1]
                tmp += 1
        answer.append(tmp)
    return max(answer)