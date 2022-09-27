T = int(input())
base = list()
for _ in range(T):
    a,b = map(int, input().split())
    base.append([a,b])

for i in base:
    cnt = 1
    for j in base:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=' ') 