import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
maps = list(list(map(int, input().split(' '))) for _ in range(n))

answer = []

minv = min(min(row) for row in maps)
maxv = max(max(row) for row in maps)

for target in range(minv, maxv+1):
    tmpb = b
    time = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] > target:
                tmpb += maps[i][j]-target
                time += 2*(maps[i][j]-target)
            else:
                tmpb -= target - maps[i][j]
                time += target - maps[i][j]
    if tmpb >= 0:
        answer.append([time, target])
        
answer.sort(key=lambda x : x[1], reverse=True)    
answer.sort(key=lambda x : x[0])

print(*answer[0])