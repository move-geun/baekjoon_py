lst = list(map(int, input().split()))
tmp = 0
for i in lst:
    tmp += i**2
print(tmp%10)