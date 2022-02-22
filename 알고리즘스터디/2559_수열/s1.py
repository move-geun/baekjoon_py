days, day = map(int,input().split())
day_list = list(map(int,input().split()))


middle = sum(day_list[:day])

temp = [middle]
for i in range(0,days-day):
    middle = middle - day_list[i] + day_list[i+day]
    temp.append(middle)

print(max(temp))


        