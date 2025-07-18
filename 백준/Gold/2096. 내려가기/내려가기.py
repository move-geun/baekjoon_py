from sys import stdin

N = int(input())

arr = list(map(int, stdin.readline().split()))
maxDP = arr
minDP = arr
for _ in range(N - 1):
    arr = list(map(int, stdin.readline().split()))
    
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] + min(minDP), arr[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))
