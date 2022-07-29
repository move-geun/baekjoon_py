lst = [0 for _ in range(10)]
num = 1
for i in range(3):
    a = int(input())
    num *= a
num = str(num)
for i in num:
    lst[int(i)] += 1
for i in lst:
    print(i)