import sys
from collections import defaultdict

input = sys.stdin.readline

dicts = defaultdict(int)
a = int(input())
a_lst = list(map(int, input().split(' ')))
b = int(input())
b_lst = list(map(int, input().split(' ')))
answer = list()
for i in a_lst:
    dicts[i] += 1

for j in b_lst:
    if dicts[j] == 0:
        answer.append(0)
    else:
        answer.append(dicts[j])
print(*answer)
