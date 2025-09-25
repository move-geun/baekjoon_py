from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if (sum1+sum2)%2 != 0:
        return -1

    while True:
        if answer == 4*len(queue1):
            return -1
        if sum1 > sum2:
            tmp1 = q1.popleft()
            q2.append(tmp1)
            sum1 -= tmp1
            sum2 += tmp1
        elif sum1 < sum2:
            tmp2 = q2.popleft()
            q1.append(tmp2)
            sum2 -= tmp2
            sum1 += tmp2
        else:
            return answer
        answer += 1
    