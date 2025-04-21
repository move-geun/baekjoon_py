import sys

input = sys.stdin.readline
k, n= map(int, input().split())
lst = []
for _ in range(k):
    num = int(input())
    lst.append(num)

si, ei = 1, max(lst)
while si<=ei:
    middle = (si+ei)//2
    tmp = 0
    for i in lst:
        tmp += i//middle
    if tmp >= n:
        si = middle+1
    else:
        ei = middle-1
    
print(ei)