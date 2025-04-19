a,b = map(int, input().split(' '))

def gcd(n,m):
    a,b = 0,0
    if n >= m:
        a,b = n,m
    else:
        a,b = m,n
    
    while b>0:
        a,b = b, a%b
    return a

print(gcd(a,b))
print(a*b//gcd(a,b))