import sys
from collections import defaultdict

input = sys.stdin.readline

hash = defaultdict(int)
n = int(input())
maps = list(map(int, input().split(' ')))

set_maps = list(set(maps))
set_maps.sort()
for idx, i in enumerate(set_maps):
    hash[i] = idx

answer = list(hash[i] for i in maps)

print(' '.join(str(x) for x in answer))