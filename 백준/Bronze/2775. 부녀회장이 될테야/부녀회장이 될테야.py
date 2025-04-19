maps = [[i+1 for i in range(14)] for _ in range(14)]
for i in range(14):
    for j in range(14):
        maps[i][j] = sum(maps[i-1][:j+1])
    
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(maps[k-1][n-1])