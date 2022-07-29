lst = list()
max_num = 0
max_index = 0
for i in range(1,10):
    a = int(input())
    lst.append(a)
    if a > max_num:
        max_num = a
        max_index = i
print(max_num)
print(max_index)

