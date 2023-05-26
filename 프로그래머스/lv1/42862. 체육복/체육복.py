def solution(n, lost, reserve):
    t_lost = list(set(lost)-set(reserve))
    t_reserve = list(set(reserve)-set(lost))
    
    for i in t_lost:
        if i-1 in t_reserve:
            t_reserve.remove(i-1)
        elif i+1 in t_reserve:
            t_reserve.remove(i+1)
        else:
            n-=1
    return n