def solution(s):
    answer = [0,0]
    
    while(True):
        tmp = ''
        for i in range(len(s)):
            if s[i] == '1':
                tmp += '1'
            else:
                answer[1] += 1
        s = str(bin(len(tmp))[2:])
        answer[0] += 1
        if s == '1':
            break
            
    return answer