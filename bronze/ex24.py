a = int(input())
lst = list(map(int, input().split()))
score = max(lst)
for i in range(0,a):
    lst[i] = lst[i]/score*100
    
print(sum(lst)/a)
