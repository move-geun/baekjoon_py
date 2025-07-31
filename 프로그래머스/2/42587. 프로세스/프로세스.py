from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append([priorities[i], True if i == location else False])
    
    while True:
        maxi = max(q)
        tmp = q.popleft()
        
        if maxi[0] == tmp[0]:
            if tmp[1]:
                return answer+1
            else:
                answer += 1
        else:
            q.append(tmp)

    return answer