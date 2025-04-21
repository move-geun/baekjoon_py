import sys
import math

input = sys.stdin.readline
t = int(input())
def change(n):
    return math.floor(n+0.5)

if t == 0:
    print(0)
else:
    si, ei = change(t*0.15), t-change(t*0.15)
    lst = []
    for _ in range(t):
        num = int(input()) 
        lst.append(num)
    lst.sort()
    print(change(sum(lst[si:ei])/(len(lst[si:ei]))))
