def solution(n):
    answer = 0
    lst = [0,1,1]
    i = 2
    while(i < n):
        i += 1
        lst.append(lst[i-1]+ lst[i-2])

    return lst[-1]%1234567