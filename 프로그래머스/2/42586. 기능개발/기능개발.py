def solution(progresses, speeds):
    answer = []
    idx = 0
    maxi = len(speeds)
    while idx < maxi:
        cnt = 0
        for i in range(idx, maxi):
            progresses[i] += speeds[i]
        
        for i in range(idx, maxi):
            if progresses[i] >= 100:
                cnt += 1
                idx += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)

    return answer