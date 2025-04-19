a,b = map(int, input().split())

lst = [1, 1, 2]
for i in range(3,a+1):
    lst.append(lst[i-1]*i)

print(lst[a]//lst[a-b]//lst[b])