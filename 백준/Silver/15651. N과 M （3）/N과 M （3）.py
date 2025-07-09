import sys

input = sys.stdin.readline

n,m = map(int, input().split())
tmp = []
def make(cnt):
    if len(tmp) == m:
        print(*tmp)
        return 
    
    for i in range(1, n+1):
        tmp.append(i)
        make(cnt+1)
        tmp.pop()
make(1)