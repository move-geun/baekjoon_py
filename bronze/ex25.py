T = int(input())

for tc in range(T):
    lst = list(map(int, input().split()))
    sum_avg = (sum(lst)-lst[0])/lst[0]
    cnt = 0
    for i in range(1,lst[0]+1):
        if lst[i] > sum_avg:
            cnt += 1
    b = round(cnt/lst[0]*100,3)
    print('{:.3f}%'.format(b))  

