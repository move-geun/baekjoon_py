M,N = map(int, input().split())
base = list()
for _ in range(M):
    row = list(input())
    base.append(row)

# 체스판 나누기
# 최소값 mini
mini = 100000000000
for i in range(M-7):
    for j in range(N-7):
        # 동시 탐색
        case1, case2 = 0, 0
        # 체스판 분석
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) %2 ==0:
                    if base[x][y] != 'W':
                        case1 += 1
                    else:
                        case2 +=1
                else:
                    if base[x][y] != 'B':
                        case1 += 1
                    else:
                        case2 += 1
        tmp_mini = min(case1, case2)
        if mini > tmp_mini :
            mini = tmp_mini
print(mini)
