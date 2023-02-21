def solution(survey, choices):
    answer = ''
    result = [[0,0] for _ in range(4)]
    score = [0,3,2,1,0,1,2,3]
    check_R = ["TR", "FC", "MJ", "NA"]
    check_T = [["R","T"], ["C","F"],["J","M"],["A","N"]]
    reverse = False
    for i in range(0,len(survey)):
        tmp = choices[i]
        if survey[i] in check_R:
            reverse = True
        if reverse:
            tmp = 8 - tmp
            
        if "R" in survey[i]:
            if tmp < 4:
                result[0][0] += score[tmp]
            else:
                result[0][1] += score[tmp]
                
        elif "C" in survey[i]:
            if tmp < 4:
                result[1][0] += score[tmp]
            else:
                result[1][1] += score[tmp]
                
        elif "J" in survey[i]:
            if tmp < 4:
                result[2][0] += score[tmp]
            else:
                result[2][1] += score[tmp]
                
        elif "A" in survey[i]:
            if tmp < 4:
                result[3][0] += score[tmp]
            else:
                result[3][1] += score[tmp]

        reverse = False

    for i in range(0,4):
        if result[i][0] >= result[i][1]:
            answer += check_T[i][0]
        elif result[i][0] < result[i][1]:
            answer += check_T[i][1]
    

    return answer