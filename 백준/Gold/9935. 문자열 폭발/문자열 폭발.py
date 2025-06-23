import sys
input = sys.stdin.readline

s = list(input().strip())
tar = list(input().strip())
cnt = len(tar)
stack = []

for i in range(len(s)):
    stack.append(s[i])

    if ''.join(stack[-cnt:]) == ''.join(tar):
        for _ in range(cnt):
            stack.pop()

if len(stack):
    print(''.join(stack))
else:
    print('FRULA')
