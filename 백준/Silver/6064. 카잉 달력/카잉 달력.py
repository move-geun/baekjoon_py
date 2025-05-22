import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m,n,x,y = map(int, input().split(' '))
    day = x
    flag = False
    while day <= m*n:
        if (day-x)%m ==0 and (day-y)%n==0:
            flag = True
            break
        day += m
    
    print(day if flag else -1)