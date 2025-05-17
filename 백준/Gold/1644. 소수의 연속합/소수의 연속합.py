import sys

input = sys.stdin.readline
n = int(input())

primes = [0]*(n+1)
for i in range(2,n+1):
    if primes[i] == 0:
        primes[i] = 1
    for j in range(i**2,n+1,i):
        primes[j] = -1

prime = [i for i,j in enumerate(primes) if j == 1]

cnt = 0
si, ei = 0, 0
tmp = 0

while si < len(prime):
    if tmp < n:
        if ei == len(prime):
            break
        tmp += prime[ei]
        ei += 1
    else:
        tmp -= prime[si]
        si += 1

    if tmp == n:
        cnt += 1
    if si == len(prime):
        break

print(cnt)