import sys
import heapq

input = sys.stdin.readline
t = int(input())
lst = []

for _ in range(t):
    nums = int(input())
    abs_nums = abs(nums)

    if nums == 0:
        # 최소힙 & 최소값 출력
        if len(lst):
            tmp = heapq.heappop(lst)
            print(tmp[1])
        else:
            print(0)
    else:
        heapq.heappush(lst, [abs_nums, nums])