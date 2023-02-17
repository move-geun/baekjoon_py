def solution(s):
    answer = []
    duple = []
    i = 0
    while i < len(s):
        if s[i] in duple:
            j = 1
            while s[i] != s[i-j]:
                j += 1
            answer.append(j)
            i += 1
        else:
            answer.append(-1)
            duple.append(s[i])
            i += 1
        
    return answer