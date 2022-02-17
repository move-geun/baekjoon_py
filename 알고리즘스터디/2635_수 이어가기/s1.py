# 100 70 30 40 10

# 100 65 35 30 5 25

# 100 63 37 26 9 17

# 100 60 40 20 20 0 20

# 100 61 39 22 17 5 12

# 100 62 38 24 14 10 4 6


first = int(input())


aws_list = list()
for i in range(int(0.617*first), int(0.619*first)+2): 
    rslt = [first, 0]
    a = 0
    # sec_list 돌면서 경우의 수 다 만들고,
    rslt[1] = i

    # 3번째 수부터는 다음 공식으로 들어갑니다.
    a = rslt[len(rslt)-2] - rslt[len(rslt)-1]

    # a가 rslt의 마지막 값보다 작을 때까지 반복시키고
    while a <= rslt[len(rslt)-1] :
        rslt.append(a)
        a = rslt[len(rslt)-2] - rslt[len(rslt)-1]

    # while 터졌을 때, 마지막과 마지막 앞 값을 rslt에 추가
    final = -(rslt[len(rslt)-1] - rslt[len(rslt)-2])
    rslt.append(final)

    # 그걸 aws_lst에 넣고
    aws_list.append(rslt)
# aws_lst 내에서 len 돌려서 가장 많이 나온것과 그 값 출력
temp = idx = 0
for i in range(len(aws_list)):
    if temp < len(aws_list[i]):
        temp = len(aws_list[i])
        idx = i

print('{}' .format(temp))
print(*aws_list[idx])