import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
lst = input().strip()
i, cnt, answer = 0,0,0

while i < m-1:
    if lst[i:i+3] == 'IOI':
        cnt += 1
        i += 2
        if cnt == n:
            answer += 1 
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(answer)