import sys
input = sys.stdin.readline

n = int(input())
lst = [1] * (n+1)
for i in range(2,n+1):
    lst[i] = lst[i-1]*i

tmp = str(lst[n])
cnt = 0
for i in range(len(tmp)-1,-1,-1):
    if tmp[i] == '0':
        cnt += 1
    else:
        break

print(cnt)