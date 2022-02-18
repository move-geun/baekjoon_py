# k가 포함된 인덱스 찾기
def ret_idx(lst,k):
    for i in range(len(lst)):
        for j in lst[i]:
            if j == k:
                return i


# 이중 리스트 내에서 최대값 구하기
def find_max(lst,idx):
    max = 0
    for i in range(len(lst)):
        # 주사위 밑면이 있는 list는 패스해라
        if i == idx:
            continue
        for j in lst[i]:
            if j > max:
                max = j
    return max


# 다음 주사위에 쓰일 윗면 값 알아내기
def for_flag(lst,idx,i):
    for flag in lst[idx]:
        if flag != i :
            return flag 



dice = int(input())
# A~F 각각 밑면으로 사용했을 때 최대합 저장소
max_list = [0,0,0,0,0,0]
# 다음 주사위 밑면이 무엇인지, 저장해 놓는 곳
flag_list = [0,0,0,0,0,0]

for tc in range(dice):
    a,b,c,d,e,f = map(int, input().split())
    # a-f, b-d, c-e 세트니까~ 묶어버림
    dice_list = [[a,f],[b,d],[c,e]]
    
    # cnt로 max_list, flag_list의 idx 컨트롤한다
    cnt = 0
    for j in range(3):
        for k in range(2):
            # 첫 시도 때 0 값 다 바꿔주고
            if tc == 0 :
                max_list[cnt] = find_max(dice_list,ret_idx(dice_list, dice_list[j][k]))
                flag_list[cnt] = for_flag(dice_list,ret_idx(dice_list, dice_list[j][k]), dice_list[j][k])
                cnt += 1
            # 나머지 때 전부 이렇게 돌린다.
            else : 
                max_list[cnt] += find_max(dice_list,ret_idx(dice_list, flag_list[cnt]))
                flag_list[cnt] = for_flag(dice_list,ret_idx(dice_list, flag_list[cnt]), flag_list[cnt])
                cnt += 1

print(max(max_list))

