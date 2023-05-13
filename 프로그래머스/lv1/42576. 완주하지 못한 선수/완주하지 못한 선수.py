from collections import defaultdict

def solution(participant, completion):
    answer = ''
    finish = defaultdict(int)
    for i in participant:
        finish[i] += 1
    for i in completion:
        finish[i] -= 1
    for i in finish:
        if finish[i] >= 1:
            answer += i
        
    return answer