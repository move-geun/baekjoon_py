import sys
input = sys.stdin.readline

from collections import deque

t = int(input())
lst = [i for i in range(1,t+1)]
lst = deque(lst)
while True:
    if len(lst) == 1:
        break
    lst.popleft()
    tmp = lst.popleft()
    lst.append(tmp)

print(lst[0])
