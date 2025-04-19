while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    maxV = max(a,b,c)
    tmp = a**2+b**2+c**2-maxV**2
    if tmp == maxV**2:
        print('right')
    else:
        print('wrong')
