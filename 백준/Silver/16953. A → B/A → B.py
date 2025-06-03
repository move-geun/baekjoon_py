import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1

while B > A:
    s = str(B)
    if s[-1] == '1':
        B = int(s[:-1])
        cnt += 1
    elif B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        print(-1)
        sys.exit(0)

print(cnt if B == A else -1)
