def solution(keymap, targets):
    answer = []
    for tar in targets:
        possible = True
        times = [10000 for _ in range(len(tar))]
        for i in range(0,len(tar)):
            for key in keymap:
                for j in range(0, len(key)):
                    if key[j] == tar[i] and times[i] > (j+1):
                        times[i] = j+1
                        break
            if times[i] == 10000:
                possible = False
        if possible:
            answer.append(sum(times))
        else:
            answer.append(-1)
    return answer