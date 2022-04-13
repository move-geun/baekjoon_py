
N = int(input())
base = list(map(int,input().split()))
ctrl_super, ctrl_sub = map(int,input().split())

ssuper,sub = 0,0
for i in range(N):
    # 응시인원이 총감독관 관리인원보다 같거나 작을 때
    # 총감독 하나면 된다
    if base[i] <= ctrl_super:    
        ssuper += 1
        continue
    # 응시인원이 총감독 관리보다 많을 경우
    # 총감독 관리인원만큼 빼고
    # 남은 인원 기준으로 보조감독 뽑는다
    else:
        base[i] = base[i] - ctrl_super
        ssuper += 1
        if base[i] % ctrl_sub:
            sub += base[i]//ctrl_sub
            sub += 1
        else:
            sub += base[i]//ctrl_sub
print(ssuper+sub)