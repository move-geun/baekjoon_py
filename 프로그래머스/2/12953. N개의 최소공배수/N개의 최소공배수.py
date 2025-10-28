def gdc(a,b):
    while b>0:
        a,b = b, a%b
    return a

def lcd(a,b):
    tmp = gdc(a,b)
    return a*b//tmp

def solution(arr):
    tmp = arr[0]
    for i in range(1, len(arr)):
        tmp = lcd(tmp, arr[i])
    return tmp