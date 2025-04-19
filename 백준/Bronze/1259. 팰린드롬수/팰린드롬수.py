while True:
    lst = list(map(str, input()))
    lst.insert(0,0)
    limit = int(len(lst)//2)
    if lst == [0, '0']:
        break
    flag = True
    for i in range(1,limit+1):
        if lst[i] != lst[i*-1]:
            flag = False
            break
    print('yes' if flag else 'no')
