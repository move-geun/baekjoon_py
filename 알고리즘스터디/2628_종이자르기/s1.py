# 1. 가로, 세로 컷 점 구하기
# 2. 각 해당 길이 중 max 구하기
# 3. 가로 max * 세로 max = 내가 원하는 답

# 가로 세로 길이 받기
N, M = map(int,input().split())
T = int(input())

# 각 cut 지점 넣을 리스트
row_list = list()
column_list = list()

# 가로 컷, 세로 컷 시점 구하기
for _ in range(T):
    direction, number = map(int,input().split())
    if direction == 0 :
        row_list.append(number)
    else :
        column_list.append(number)

# sort하기
row_list.sort()
column_list.sort()

# 양 끝 범위 넣기 (시작 부분에 0, 끝부분에 N과 M)
row_list.insert(0,0)
column_list.insert(0,0)
row_list.append(M)
column_list.append(N)

# 각 최대값 구하기
def max_dif(lst):
    temp = 0
    for i in range(1,len(lst)):
        if lst[i]-lst[i-1] >= temp:
            temp = lst[i]-lst[i-1]
    return temp

print(max_dif(row_list)*max_dif(column_list))


