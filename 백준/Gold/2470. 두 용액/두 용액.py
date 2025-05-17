import sys

input = sys.stdin.readline
N = int(input())
acids = list(map(int, input().split(' ')))
acids.sort()
si,ei = 0, len(acids)-1
now = 2000000000
answer = []
while si<ei:
    tmp = acids[si]+acids[ei]
    if abs(tmp) < now:
        now = abs(tmp)
        answer = [acids[si], acids[ei]]
    
    if tmp < 0:
        si += 1
    else:
        ei -= 1

print(*answer)