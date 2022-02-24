
base_list = list()
call_num = list()


# 빙고 배열 받기
for _ in range(5):
    temp_base = list(map(int,input().split()))
    base_list.append(temp_base)

# 사회자 콜넘버 받기
for z in range(5):
    temp_bingo = list(map(int,input().split()))
    call_num += temp_bingo

ans = 0
for i in range(25):
    for j in range(5):
        for k in range(5):
            if base_list[j][k] == call_num[i]:
                base_list[j][k] = 0
    ans += 1
    line = 0
    if ans > 11:
        for r in range(5):
            r_sum = 0
            for q in range(5):
                r_sum += base_list[r][q]
            
            if r_sum == 0 :
                line += 1

        for w in range(5):
            c_sum = 0
            for e in range(5):
                c_sum += base_list[e][w]
            if c_sum == 0 :
                line += 1
        

        dig_sum = 0
        xdig_sum = 0
        for p in range(5):
            dig_sum += base_list[p][p]
            xdig_sum += base_list[4-p][p]
        if dig_sum == 0 :
            line += 1
        if xdig_sum == 0 :
            line += 1
                
    if line >= 3 :
        break

print(ans)