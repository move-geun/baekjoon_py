N, K = map(int, input().split())
base = [int(input()) for _ in range(N)]
cnt = 0
for i in range(1,N+1):
    if (K// base[-i]) != 0:
        cnt += K//base[-i]
        K %= base[-i]

print(cnt)