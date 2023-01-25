import sys

N = int(sys.stdin.readline())

now = 0
line = 0
while now < N:
    line += 1
    now += line

dif = now - N
if line % 2: # 홀수
    print(f"{1+dif}/{line-dif}")
else: # 짝수
    print(f"{line-dif}/{1+dif}")