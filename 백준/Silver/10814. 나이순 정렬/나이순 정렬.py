import sys
input = sys.stdin.readline

lst = []
T = int(input())
for t in range(T):
    age, name = input().strip().split(' ')
    lst.append([int(age), t, name])
sorted_lst = sorted(lst, key = lambda x:(x[0], x[1]))

for i in sorted_lst:
    print(f'{i[0]} {i[2]}')