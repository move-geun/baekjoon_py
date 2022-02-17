
# 남자면 숫자 배수에 스위치 상태 변경
def boy(lst,num):
    for i in range(num-1,len(lst),num):
        if lst[i] == 0 :
            lst[i] = 1
        else :
            lst[i] = 0


def girl(lst,num):
    # 몇 번까지 돌리는게 안전한지 
    safe_cnt = num-1
    if num-1 > len(lst)-num :
        safe_cnt = len(lst)-num
    
    # safe_cnt 기준으로 while 시작(몇 번이나 같은지 확인)
    cnt = 1
    i = 0 
    # 인덱스 맞추기 위해 lst[num-1-cnt]
    while cnt <= safe_cnt :
        if lst[num-1-cnt] == lst[num-1+cnt]:
            i += 1
        else :
            break
        cnt += 1
    
    # idx가 하나 밀려있으니까 ex) num이 3이고 i가 2일때, 0~4 indx까지 바꿔야한다
    for j in range(num-i-1,num+i):
        if lst[j] == 0:
            lst[j] = 1
        else:
            lst[j] = 0
        

# T = 스위치 갯수
# switch 상태 리스트
# 몇 명의 학생이 오는지
# 성별과 받은 번호 확인
T = int(input())
switch = list(map(int,input().split()))
times = int(input())
for _ in range(times):
    gender, number = map(int,input().split())
    if gender == 1 :
        boy(switch,number)
    else :
        girl(switch,number)

# 20개씩 끊어 출력하기
start = 0
for i in range(start,T,20):
    final = switch[start:start+20]
    if final != []:
        print(*final)
    start += 20

