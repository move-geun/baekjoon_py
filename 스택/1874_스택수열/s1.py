import sys

N = int(sys.stdin.readline())
base = list(int(sys.stdin.readline()) for _ in range(N)) 
stack = list()
tmp = list()
aws = list()
j = 0
for i in range(1, N+1):
    if i != base[j]:
        stack.append(i)
        aws.append('+')

    elif i == base[j]:
        aws.append('+')
        tmp.append(i)
        j += 1
        aws.append('-')
        while stack and (stack[-1] == base[j]):
            aws.append('-')
            tmp.append(base[j])
            del stack[-1]
            j += 1
            if j == N:
                break

if base != tmp:
    print("No")
else:
    for i in range(len(aws)):
        print(aws[i])
