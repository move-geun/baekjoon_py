import sys

N = int(sys.stdin.readline())
cnt = 0 
for i in range(N):
    st = list(sys.stdin.readline())
    duple = list()
    tmp = ''
    AWS = True
    for j in st:
        if tmp == j:
            continue
        elif tmp != j:
            tmp = j
            if j not in duple:
                duple.append(j)
            elif j in duple:
                AWS = False
                break
    if AWS:
        cnt += 1
print(cnt)


