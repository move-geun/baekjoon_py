import sys

N = int(sys.stdin.readline())

def sol(M):
    cnt = 0
    for i in range(1,M+1):
        base = list(str(i))
        if i < 100:
            cnt += 1
        else:
            if int(base[0])-int(base[1]) == int(base[1])-int(base[2]):
                cnt += 1
    return cnt

print(sol(N))

