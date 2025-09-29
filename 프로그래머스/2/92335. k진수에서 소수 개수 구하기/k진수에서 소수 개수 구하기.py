def change(n,q):
    tmp = ''
    while n>0:
        n,mod = divmod(n,q)
        tmp += str(mod)
    return tmp[::-1]

def isPrime(n):
    if n < 2:
        return False
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    n = change(n,k)
    lst = n.split('0')
    for i in lst:
        if len(i) and isPrime(int(i,10)):
            answer += 1
    return answer