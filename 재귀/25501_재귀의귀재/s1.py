import sys

def sol(lst,l,r):
    global cnt
    global aws
    cnt += 1
    if l >= r:
        aws = 1
    elif lst[l] != lst[r]:
        aws = 0
    else:
        sol(lst,l+1,r-1)

N = int(sys.stdin.readline())
for i in range(N):
    S = list(input())
    cnt = 0
    aws = 0
    sol(S,0,len(S)-1)
    print(f'{aws} {cnt}')

