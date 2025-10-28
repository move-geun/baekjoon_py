def solution(order):
    answer = 0
    
    stack = []
    idx = 0
    for i in range(1, len(order) + 1):
        stack.append(i)
        while (stack) and (stack[-1] == order[idx]):
            answer += 1
            idx += 1
            stack.pop()

    return answer