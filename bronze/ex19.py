a = int(input())
cnt = 0
d = a
while True:
    b = d//10
    c = d%10
    d = (b+c)%10+c*10
    cnt += 1
    if d == a:
        break
print(cnt)

