def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        flag = True
        day = startday-1
        for j in range(7):
            day += 1
            if day >= 8:
                day = 1
            if day == 6 or day == 7:
                continue
            lim = schedules[i] + 10
            if lim%100 >= 60:
                lim = lim + 40
            real = timelogs[i][j]
            if lim < real:
                flag = False
                break

        if flag:
            answer += 1

    return answer