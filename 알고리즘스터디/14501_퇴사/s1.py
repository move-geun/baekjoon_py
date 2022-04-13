
def dfs(day, pay):
    global max_pay

    # 종료조건
    if day == N and Ti[day] == 1:
        pay += Pi[day]

    if day >= N:
        if max_pay < pay:
            max_pay = pay
        return

    # 도는조건
    # 업무시작일부터 하루씩 카운트 되서 종료 시점을 N+1로 잡아줌
    if day+Ti[day] <= N+1:
        dfs(day+Ti[day], pay+Pi[day])
    # 해당 날짜 일 선택 안하고 넘어갈 수 있으니까
    if day+1 <= N:
        dfs(day+1, pay)
    # N 범위를 넘어버리면 값 더하지 말고 끝내자
    else:
        dfs(day+Ti[day],pay)

N = int(input())
Ti = [0]
Pi = [0]
max_pay = -1
for _ in range(N):
    a, b = map(int, input().split())
    Ti.append(a)
    Pi.append(b)
dfs(1,0)

print(max_pay)

