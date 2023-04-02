from collections import deque

def solution(plans):
    answer = []
    plans.sort(key = lambda x:x[1])
    todo = deque()
    now = int(plans[0][1][:2])*60 + int(plans[0][1][3:])

    for i in range(0,len(plans)-1):
        # 다음 공부 시작 전에 끝낼 때
        if int(plans[i][1][:2])*60 + int(plans[i][1][3:]) + int(plans[i][2]) <= int(plans[i+1][1][:2])*60 + int(plans[i+1][1][3:]):
            now += int(plans[i][2]) 
            plans[i][2] = 0
            answer.append(plans[i][0])
            while todo:
                plan = todo.pop()
                if now + plan[2] <= int(plans[i+1][1][:2])*60 + int(plans[i+1][1][3:]):
                    answer.append(plan[0])
                    now += plan[2] 
                elif now + plan[2] > int(plans[i+1][1][:2])*60 + int(plans[i+1][1][3:]):
                    plan[2] = now + plan[2] - (int(plans[i+1][1][:2])*60 + int(plans[i+1][1][3:]))
                    now = int(plans[i+1][1][:2])*60 + int(plans[i+1][1][3:])
                    todo.append(plan)
                    break
                  
        # 다음 공부 시작될 때
        else:
            plans[i][2] = (int(plans[i][1][:2])*60 + int(plans[i][1][3:]) + int(plans[i][2])) - (int(plans[i+1][1][:2])*60 + int(plans[i+1][1][3:]))
            todo.append(plans[i])
            now =int(plans[i+1][1][:2])*60 + int(plans[i+1][1][3:])
        

    answer.append(plans[-1][0])
    plans[-1][2] = 0

    while todo:
        plan = todo.pop()
        answer.append(plan[0])


        
    return answer