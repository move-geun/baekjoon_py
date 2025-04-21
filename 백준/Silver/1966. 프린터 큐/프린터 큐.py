import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, i = map(int, input().strip().split(' '))
    tmp = list(map(int, input().strip().split(' ')))
    lst = list([tmp[k],0] if k != i else [tmp[k],1] for k in range(len(tmp)))
    q = deque(lst)
    
    idx = 1
    while q:
        tmp = max(q)
        left = q.popleft()
        # 가장 왼쪽 값이 가장 크면서(삭제될 기회면서) 우리의 찾는 값일 때 
        if tmp[0] == left[0] and left[1] == 1:
            print(idx)
            break
        # 가장 왼쪽 값이 가장 크면서(삭제될 기회면서) 우리가 찾는 값이 아닐 때
        elif tmp[0] == left[0] and left[1] == 0:
            idx += 1
        # 가장 왼쪽 값이 가장 크지 않을 때1
        else:
            q.append(left)