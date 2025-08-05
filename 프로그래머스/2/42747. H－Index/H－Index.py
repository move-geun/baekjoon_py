def solution(citations):
    citations.sort()
    cnt = 1
    maxi = len(citations)
    
    while cnt <= maxi:
        if citations[maxi-cnt] >= cnt:
            cnt += 1
        else:
            break
    return cnt-1

