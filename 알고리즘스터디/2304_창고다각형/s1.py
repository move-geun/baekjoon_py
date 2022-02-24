T = int(input())

max_h = 0
max_idx = 0
warehouse = list()
total = 0

# 창고 건물 받고, 순서대로 정렬
for _ in range(T):
    w,h = map(int,input().split())
    if h > max_h:
        max_h = h
    warehouse.append([w,h])

warehouse.sort()

# 최대 높이 건물 인덱스 찾기
for i in range(T):
    if warehouse[i][1] == max_h:
        max_idx = i

# 왼쪽부터 검색
h = 0
for j in range(max_idx):
    if warehouse[j][1] > h :
        h = warehouse[j][1]
    total += (warehouse[j+1][0] - warehouse[j][0]) * h

# 오른쪽 검색
h = 0
for k in range(T-1,max_idx,-1):
    if warehouse[k][1] > h :
        h = warehouse[k][1]
    total += (warehouse[k][0] - warehouse[k-1][0]) * h

total += max_h

print(total)