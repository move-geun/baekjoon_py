n = int(input())
lst = list(map(str, input()))
points = [i for i in range(1,27)]

tmp = 0
for i in range(len(lst)):
    idx = ord(lst[i])-97
    tmp += points[idx]*(31**i)

print(tmp%1234567891)