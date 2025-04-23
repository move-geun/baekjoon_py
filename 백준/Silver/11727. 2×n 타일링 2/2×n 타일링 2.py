import sys
input = sys.stdin.readline

t = int(input()) 
maps = [0,1,3]
for i in range(3, t+1):
    maps.append(maps[i-2]*2+maps[i-1])
print(maps[t]%10007)