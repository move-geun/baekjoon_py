N = int(input())
# 666 후보들 넣기
ans_cani = list()
# 정답 인덱스
ans_idx = N-1
# 666 찾기
for i in range(2700000):
    find = list(str(i))
    for j in range(len(find)-2):
        if find[j] == '6' and find[j+1] == '6' and find[j+2]=='6':
            ans_cani.append(i)
            pass
ans_cani = list(set(ans_cani))
ans_cani.sort()
print(ans_cani[ans_idx])