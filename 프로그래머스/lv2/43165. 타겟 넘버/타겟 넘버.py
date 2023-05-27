def solution(numbers, target):
    answer = 0
    def DFS(cnt,i):
        if i == len(numbers):
            if cnt == target:
                nonlocal answer
                answer += 1
            return 
        DFS(cnt+numbers[i],i+1)
        DFS(cnt-numbers[i],i+1)
    
    DFS(0,0)
    print(answer)

    return answer