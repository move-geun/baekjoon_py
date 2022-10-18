import sys

N = int(sys.stdin.readline())
base = list()
for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        del base[-1]
    else:
        base.append(tmp)

print(sum(base))