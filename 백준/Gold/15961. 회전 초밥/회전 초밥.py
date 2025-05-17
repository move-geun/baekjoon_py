import sys

input = sys.stdin.readline
n,d,k,c = map(int, input().split(' '))
nums = [int(input()) for _ in range(n)]
for i in range(k):
    nums.append(nums[i])
lst = []

plate = [0]*(d+1)
first = 0
# 첫 윈도우
for i in range(k):
    if plate[nums[i]] == 0:
        first += 1
    plate[nums[i]] += 1

maxi = first + (1 if plate[c]==0 else 0)

for i in range(1, n):
    plate[nums[i-1]] -= 1
    if plate[nums[i-1]] == 0:
        first -= 1
    
    if plate[nums[(i+k-1)]] == 0:
        first += 1
    plate[nums[(i+k-1)]] += 1
    tmp = first + (1 if plate[c]==0 else 0)

    maxi = max(maxi, tmp)

print(maxi)
