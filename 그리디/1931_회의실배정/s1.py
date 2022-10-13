# base = [6, 3, 11, 2, 0, 2, 4, 0, 3, 0, 0, 0, 2, 0, 0]
# max_time = 14
# duplicate = [1,1,1]


N = int(input())
# 최대 회의 시간
max_time = 0
# 각 시간별 회의 소요 시간 담은 list
time_base = list()
# 회의 시작시간이랑 끝시간이 같으면 cnt 추가해줘야해서 따로 체크해놓음
duplicate = list()

# input 받기
for _ in range(N):
    start, end = map(int, input().split())
    # 회의시작시간 끝시간 같음
    if start == end:
        duplicate.append(start);
    # 각 시간별 회의 소요 시간 담기
    time_base.append([start, end-start])
    # 회의 마지막 시간 찾는거 (base 리스트 만들기용)
    if max_time < end:
        max_time = end

# 회의 끝 시간 찾아서 해당 시간만큼 0 base 만들기
base = [ 0 for _ in range(max_time+1)]

# 각 시각별 최소 소요시간 넣기
for i in range(N):
    if base[time_base[i][0]]:
        if base[time_base[i][0]] > time_base[i][1]:
            base[time_base[i][0]] = time_base[i][1]
    else: 
        base[time_base[i][0]] = time_base[i][1]

print(time_base)
print(base)
print(duplicate)


max_cnt = 0

# 각 시각별로 도는데
for i in range(len(base)):
    cnt = 0 
    # 소요시간만큼 i 추가해서 검색 줄여줌
    while i < (max_time+1):
        # 회의 시작 시간이랑 끝시간이 같으면 그만큼 cnt는 추가해줘야함
        for a in range(len(duplicate)):
            if duplicate[a] == i :
                cnt +=1
        # 값이 있다? cnt도 추가
        if base[i]:
            i += base[i]
            cnt += 1
        # 값이 없다? 다음 회의시간으로 넘기기
        else:
            i += 1
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)


