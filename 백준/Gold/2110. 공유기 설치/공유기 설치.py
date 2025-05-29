import sys

input = sys.stdin.readline

n,c = map(int, input().split(' '))
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()

si,ei = 1, lst[-1]-lst[0]
ans = 0

while si <= ei:
    middle = (si+ei)//2
    house = lst[0]
    cnt = 1

    for i in lst[1:]:
        if i-house >= middle:
            cnt += 1
            house = i
    
    if cnt >= c:
        ans = middle
        si = middle+1
    else:
        ei = middle-1

print(ans)