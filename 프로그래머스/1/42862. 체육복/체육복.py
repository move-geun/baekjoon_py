def solution(n, lost, reserve):
    lst = [1]*(n+1)
    
    for i in lost:
        lst[i] -= 1
    
    for i in reserve:
        lst[i] += 1
    
    for i in range(1, n+1):
        if lst[i] ==2:
            if i>1 and lst[i-1] == 0:
                lst[i-1] = 1
                lst[i] = 1
            elif i < n and lst[i+1] == 0:
                lst[i] = 1
                lst[i+1] = 1

    return sum(1 for x in lst[1:] if x >= 1)