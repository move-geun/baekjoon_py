
def find(i,j):
    global time
    over = False
    ni = i
    nj = j
    snake.append([ni,nj])
    
    for k in go:
        if over==True:
            break
        for m in k:
            if over==True:
                break
            di = 0
            dj = 1
            limit = k[0]
            where = k[1]
            if time>limit:
                if where=='D':
                    di = 1
                    dj = 0
                elif where=='L':
                    di = 0
                    dj = -1
            while time<=limit:
                ni += di
                nj += dj

                #종료조건
                if base[ni][nj]==0:
                    over = True
                    break
                if base[ni][nj] in snake:
                    over = True
                    break

                # 도는 조건
                if 1 <= ni < N and 1 <= nj < N:
                    if base[ni][nj] == 1:
                        snake.append([ni,nj])
                        time += 1
                    else:
                        snake.append([ni,nj])
                        snake.pop(0)
                        time += 1

N = int(input())
# base 만들기
base = [[0 for _ in range(N+2)]]
for _ in range(N):
    base.append([0]+[3 for _ in range(N)] + [0])
base.append([0 for _ in range(N+2)])

# 사과 위치 넣기
K = int(input())
for _ in range(K):
    a,b = map(int, input().split())
    base[a][b] = 1

# 방향 리스트 넣기
L = int(input())
go = list()
for _ in range(L):
    c,d = map(str, input().split())
    go.append([int(c),d])

time = 0
snake = list()
find(1,1)
print(time)