def solution(numbers, target):
    answer = 0
    
    def dfs(cur, idx):
        nonlocal answer
        if idx == len(numbers):
            if cur == target:
                answer += 1
                return 
            return

        dfs(cur+numbers[idx], idx+1)
        dfs(cur-numbers[idx], idx+1)
    
    dfs(0,0)
    return answer