all = set(i for i in range(1,10001))
noself = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    noself.add(i)

self_num = sorted(all-noself)
for i in self_num:
    print(i)

