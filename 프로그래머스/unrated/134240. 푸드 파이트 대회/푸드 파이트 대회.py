def solution(food):
    answer = ''
    for i in range(1,len(food)):
        j = food[i]//2
        for _ in range(0,j):
            answer += str(i)
    answer += '0'
    for i in range(len(food)-1,0,-1):
        j = food[i]//2
        for _ in range(j,0,-1):
            answer += str(i)
    
    return answer