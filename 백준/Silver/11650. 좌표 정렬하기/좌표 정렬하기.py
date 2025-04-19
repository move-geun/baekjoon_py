import sys
input = sys.stdin.readline

lst = []
T = int(input())
for t in range(T):
    x, y = map(int, input().strip().split())
    lst.append([x,y])
sorted_lst = sorted(lst, key = lambda x:(x[0], x[1]))

for i in sorted_lst:
    print(f'{i[0]} {i[1]}')