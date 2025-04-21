import sys
from collections import Counter
import math
input = sys.stdin.readline
t = int(input())
lst = [int(input()) for _ in range(t)]
tmp = Counter(lst)
lst.sort()
sorted_tmp = sorted(tmp.items(), key=lambda x : (-x[1], x[0]))
most_cnt = sorted_tmp[0][1]

# 정답
print(math.floor(sum(lst)/t+0.5))
print(lst[t//2])
print(sorted_tmp[1][0] if len(lst) >=2 and sorted_tmp[1][1] == most_cnt else sorted_tmp[0][0])
print(lst[-1]-lst[0])