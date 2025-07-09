import sys

input = sys.stdin.readline

n,m = map(int, input().split())
tmp = []
def make(cnt):
    if cnt == m:
        print(*tmp)
        return 
    for i in range(1, n+1):
        if i not in tmp:
            tmp.append(i)
            make(cnt+1)
            tmp.pop()

make(0)