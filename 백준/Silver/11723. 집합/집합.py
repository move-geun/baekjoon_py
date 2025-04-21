import sys
input = sys.stdin.readline
t = int(input())
s = []
for _ in range(t):
    lst = list(input().split())
    if lst[0]=='add':
        if int(lst[1]) not in s:
            s.append(int(lst[1]))
    elif lst[0]=='remove':
        if int(lst[1]) in s:
            s.remove(int(lst[1]))
    elif lst[0] == 'check':
        print(1 if int(lst[1]) in s else 0)
    elif lst[0] == 'toggle':
        if int(lst[1]) in s:
            s.remove(int(lst[1]))
        else:
            s.append(int(lst[1]))
    elif lst[0] == 'all':
        s = [i for i in range(1,21)]
    elif lst[0] == 'empty':
        s = []
