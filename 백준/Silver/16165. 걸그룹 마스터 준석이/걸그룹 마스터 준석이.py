import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
li = defaultdict(list)

for _ in range(N):
    group = input().strip()
    num = int(input().strip())
    for _ in range(num):
        name = input().strip()
        li[group].append(name)

li = dict(li)

for _ in range(M):
    quiz_name = input().strip()
    quiz_num = int(input().strip()) 

    if quiz_num == 1:
        for key, values in li.items():
            if quiz_name in values:
                print(key)
                break
    elif quiz_num == 0:
        for key, values in li.items():
            if quiz_name == key:
                for j in sorted(values):  
                    print(j)
                break
