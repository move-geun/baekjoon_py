import sys
input = sys.stdin.readline

a,b = map(int, input().split(' '))
a_lst = [ input().strip() for _ in range(a)]
b_lst = [ input().strip() for _ in range(b)]

tmp = list(set(a_lst)&set(b_lst))
tmp.sort()
print(len(tmp))
for i in tmp:
    print(i)