import sys

N,M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M,K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

print(A)
print(B)