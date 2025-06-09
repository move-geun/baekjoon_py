import sys

N = int(sys.stdin.readline())
stack = list()
aws = list()
real = True
count = 1
for _ in range(N):
    num = int(sys.stdin.readline())
    while count <= num:
        stack.append(count)
        aws.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        aws.append('-')
    else:
        real = False

if real == False:
    print("NO")
else:
    for i in aws:
        print(i)
