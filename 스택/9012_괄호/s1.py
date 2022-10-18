N = int(input())
for _ in range(N):
    base = list(input())
    tmp = 0
    for i in base:
        if i == '(':
            tmp += 1
        elif i == ')':
            tmp -= 1
        if tmp < 0:
            print('NO')
            break
    if tmp > 0:
        print('NO')
    elif tmp == 0:
        print('YES')
