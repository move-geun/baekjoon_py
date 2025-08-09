def solution(n, lost, reserve):
    lst = [1]*(n+1)
    ans = 0
    t_lost, t_reserve = sorted(set(lost)-set(reserve)), sorted(set(reserve)-set(lost)) 
    for i in t_lost:
        lst[i] -= 1
    for j in t_reserve:
        if lst[j] == 0:
            lst[j] += 1
        elif j == 1 and lst[j+1] == 0:
            lst[j+1] += 1
        elif lst[j-1] == 0:
            lst[j-1] += 1
        elif j < n and lst[j+1] == 0:
            lst[j+1] += 1
    return sum(lst[1:])