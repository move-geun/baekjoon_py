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
    if day+Ti[day] <= N+1:
        dfs(day+Ti[day], pay+Pi[day])
    if day+1 <= N:
        dfs(day+1, pay)
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