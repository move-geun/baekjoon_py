lst = list()
for i in range(10):
    a = int(input())
    b = a%42
    if b not in lst:
        lst.append(b)
print(len(lst))
