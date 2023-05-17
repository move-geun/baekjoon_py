def solution(progresses, speeds):
    answer = []
    day, tmp = 0, 0
    for i in range(len(progresses)):
        if progresses[i] + speeds[i] * day < 100:
            answer.append(tmp)
            tmp = 0
            while progresses[i] + speeds[i] * day < 100:
                day += 1
        tmp += 1
        if i == len(progresses) -1 :
            answer.append(tmp)    
    return answer[1:]