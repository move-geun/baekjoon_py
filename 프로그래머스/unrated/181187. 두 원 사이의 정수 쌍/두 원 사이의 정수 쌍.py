from math import ceil,floor,sqrt

def solution(r1, r2):
    cnt = 0
    for y in range(1, r2+1):
        max_x = floor(sqrt(r2**2 - y**2))
        min_x = ceil(sqrt(r1**2 - y**2)) if r1 > y else 0
        cnt += max_x - min_x + 1
    return cnt * 4