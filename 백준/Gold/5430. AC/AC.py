import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ops = input().strip()
    n   = int(input())
    arr = input().strip()
    dq = deque(arr[1:-1].split(',')) if n else deque()

    rev = False
    error = False
    for op in ops:
        if op == 'R':
            rev = not rev
        else:  # 'D'
            if not dq:
                print('error')
                error = True
                break
            dq.pop() if rev else dq.popleft()

    if error:
        continue

    if rev:
        dq.reverse()
    print('[' + ','.join(dq) + ']')
