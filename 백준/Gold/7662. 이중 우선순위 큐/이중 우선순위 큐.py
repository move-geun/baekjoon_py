import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    min_lst = []
    max_lst = []
    alive = defaultdict(int)
    for _ in range(k):
        order, nums = map(str, input().split(' '))
        nums = int(nums)
        if order == 'I':
            heapq.heappush(min_lst, nums)
            heapq.heappush(max_lst, nums*-1)
            alive[nums] += 1
        else:
            if min_lst:
                # 최솟값 삭제
                if nums == -1:
                    while min_lst and alive[min_lst[0]] == 0:
                        heapq.heappop(min_lst)
                    if min_lst:
                        tmp = heapq.heappop(min_lst)
                        alive[tmp] -= 1
                # 최댓값 삭제
                else:
                    while max_lst and alive[max_lst[0]*-1] == 0:
                        heapq.heappop(max_lst)
                    if max_lst:
                        tmp = heapq.heappop(max_lst)
                        alive[tmp*-1] -= 1
        
    # 최종 정리
    while min_lst and alive[min_lst[0]] == 0:
        heapq.heappop(min_lst)
    while max_lst and alive[max_lst[0]*-1] == 0:
        heapq.heappop(max_lst)
    
    if min_lst:
        print(max_lst[0]*-1, min_lst[0])
    else:
        print('EMPTY')