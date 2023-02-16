def solution(cards1, cards2, goal):
    answer = ''
    one_flag = two_flag = 0
    flag = True
    
    for i in goal:
        if i == cards1[one_flag]:
            if one_flag < len(cards1)-1:
                one_flag += 1
        elif i == cards2[two_flag]:
            if two_flag < len(cards2)-1:
                two_flag += 1
        else:
            flag = False
            break
    
    if flag:
        answer = "Yes"
    else:
        answer = "No"
    
    return answer