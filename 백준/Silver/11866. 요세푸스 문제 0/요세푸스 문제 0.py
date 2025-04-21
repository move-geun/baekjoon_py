import sys

input = sys.stdin.readline
n,k = map(int, input().split(' '))
tmp = k-1
lst = [i for i in range(1, n+1)]
answer = []
while (lst):
    if tmp >= len(lst):
        tmp = tmp%len(lst)
    answer.append(lst[tmp])
    lst.remove(lst[tmp])
    tmp += k-1
print(f'<{", ".join(map(str, answer))}>')