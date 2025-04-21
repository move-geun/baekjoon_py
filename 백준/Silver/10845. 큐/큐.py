import sys
from collections import deque

input = sys.stdin.readline
q = deque()
t = int(input())
for _ in range(t):
    lst = list(input().strip().split(' '))
    if lst[0] == 'push':
        q.append(int(lst[1]))
    elif lst[0] == 'pop':
        print(q.popleft() if len(q) else -1)
    elif lst[0] == 'size':
        print(len(q))
    elif lst[0] == 'empty':
        print(0 if len(q) else 1)
    elif lst[0] == 'front':
        print(q[0] if len(q) else -1)
    elif lst[0] == 'back':
        print(q[-1] if len(q) else -1)