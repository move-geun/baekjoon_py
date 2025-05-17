import sys

input = sys.stdin.readline
n, s = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

si, ei = 0,0
tmp = 0
mini = n+1

for ei in range(n):
    tmp += nums[ei]

    while tmp >= s:
        mini = min(mini, ei-si+1)
        tmp -= nums[si]
        si += 1
        
if mini == n+1:
    print(0)
else:
    print(mini)
