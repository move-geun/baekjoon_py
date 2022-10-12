# N = 10
# K = 4790
# base = [1,5,10,50,100,500,1000,5000,10000,50000]

N, K = map(int, input().split())
base = [int(input()) for _ in range(N)]
cnt = 0
for i in range(1,N+1):
    if (K// base[-i]) != 0:
        cnt += K//base[-i]
        K %= base[-i]

# 시간초과
# while K != 0:
#     for i in range(len(base)):
#         if base[i] > K:
#             cnt += K // base[i-1]
#             K %= base[i-1] 
#             base = base[:i]
#             break

print(cnt)

