import sys

N = int(sys.stdin.readline())
base = sorted(list((map(int, sys.stdin.readline().split()))))

aws = tmp =0
for i in range(N):
    tmp += base[i]
    aws += tmp
print(aws)