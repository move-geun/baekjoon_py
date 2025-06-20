N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]
 
tmp = 0 
for i in nums:
    tmp += i
    prefix_sum.append(tmp)

for _ in range(M):
    i,j = map(int, input().split())
    print(prefix_sum[j]-prefix_sum[i-1])