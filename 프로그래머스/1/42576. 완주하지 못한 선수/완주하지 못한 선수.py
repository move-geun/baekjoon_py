from collections import defaultdict
def solution(participant, completion):
    tmp = defaultdict(int)
    for i in participant:
        tmp[i] += 1
    
    for j in completion:
        tmp[j] -= 1
    ttmp = list(tmp.values()).index(1)
    
    return list(tmp.keys())[ttmp]
