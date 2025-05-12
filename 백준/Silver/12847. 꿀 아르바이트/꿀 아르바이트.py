import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))

current_sum = sum(lst[:m])
max_sum = current_sum

for i in range(m, n):
    current_sum += lst[i] - lst[i - m]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)