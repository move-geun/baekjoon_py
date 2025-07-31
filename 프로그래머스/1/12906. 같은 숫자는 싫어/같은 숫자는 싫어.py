def solution(arr):
    stack = []
    stack.append(arr[0])
    
    for i in arr:
        tmp = stack.pop()
        if i != tmp:
            stack.append(tmp)
            stack.append(i)
        else:
            stack.append(tmp)
            
    return stack