import sys
input = sys.stdin.readline

a = int(input())
maps = set(map(int, input().split()))
b = int(input())
lst = (map(int, input().split()))
for i in lst:
    print(1 if i in maps else 0)