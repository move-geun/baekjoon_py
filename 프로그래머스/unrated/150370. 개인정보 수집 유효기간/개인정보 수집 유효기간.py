def solution(today, terms, privacies):
    answer = []
    term = {}
    now_y, now_m, now_d = map(int, today.split('.'))
    
    # 약관 정리
    for i in terms:
        key, info = i.split(' ')
        term[key] = int(info)
    
    for i in range(0, len(privacies)):
        day, kind = privacies[i].split(' ')
        tmp_y, tmp_m, tmp_d = map(int,day.split('.'))
        
        # 약관 날짜 더하기
        if tmp_d == 1:
            tmp_d = 28
            tmp_m -= 1
        else:
            tmp_d -= 1
        
        tmp_m += term[kind]
        if tmp_m >= 12:
            if not tmp_m % 12:
                tmp_y += (tmp_m//12)-1
                tmp_m = 12
                
            else:
                tmp_y += tmp_m//12
                tmp_m %= 12
                
        # 현재 날짜랑 비교
        if (now_y*10000 + now_m*100 + now_d) > (tmp_y*10000 + tmp_m*100 + tmp_d):
            answer.append(i+1)
            
    return answer
