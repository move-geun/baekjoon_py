import sys
input = sys.stdin.readline

po = dict()
num = dict()

n,m = map(int, input().split(' '))
for i in range(1,n+1):
    name = input().strip()
    po[name] = i
    num[i] = name

for _ in range(m):
    tmp = input().strip()
    if tmp.isdigit():
        print(num[int(tmp)])
    else:
        print(po[tmp])