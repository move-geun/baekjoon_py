def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        cnt = 0
        for j in range(1,int(i**0.5)+1):
            if j**2 == i:
                cnt += 1
            elif i % j == 0:
                cnt += 2
        if cnt <= limit:
            answer += cnt
        else:
            answer += power
    return answer