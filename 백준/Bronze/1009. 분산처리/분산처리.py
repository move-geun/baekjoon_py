T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    base = a%10

    if base == 0:
        print(10)
    elif base in [1,5,6]:
        print(base)
    elif base in [4,9]:
        if b%2:
            print(base)
        else:
            print(base**2%10)
    else:
        if b%4:
            print(base**(b%4)%10)
        else:
            print(base**4%10)