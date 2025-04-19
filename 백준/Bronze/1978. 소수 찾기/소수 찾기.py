n = int(input())
lst = map(int, input().split(' '))

def isPrime(n):
    if n < 2:
        return False
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True

answer = 0
for i in lst:
    if isPrime(i):
        answer += 1

print(answer)
