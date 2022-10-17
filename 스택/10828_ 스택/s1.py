import sys

N = int(sys.stdin.readline())
stack = list()
base = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    if len(base[i]) > 1:
        if base[i][0] == 'push':
            stack.append(base[i][1])
        elif base[i][0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
                del stack[-1]
        elif base[i][0] == 'size':
            print(len(stack))
        elif base[i][0] == 'empty':
            if len(stack):
                print(0)
            else:
                print(1)
        else:
            if len(stack):
                print(stack[-1])
            else:
                print(-1)
    else:
        if base[i][0] == 'push':
            stack.append(base[i][1])
        elif base[i][0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
                del stack[-1]
        elif base[i][0] == 'size':
            print(len(stack))
        elif base[i][0] == 'empty':
            if len(stack):
                print(0)
            else:
                print(1)
        else:
            if len(stack):
                print(stack[-1])
            else:
                print(-1)
