def solution(n):
    answer = 0
    i = 1
    while(i < n+1):
        tmp = i
        for j in range(i+1, n+2):

            if tmp > n:
                break
            if tmp == n:
                answer += 1
                break
            else:
                tmp += j
        i += 1
        
    return answer