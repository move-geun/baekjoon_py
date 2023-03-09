def solution(n, m, section):
    answer = 0
    while section:
        start = section[0]
        end = start + m -1
        
        while section:
            if section[0] <= end:
                section.remove(section[0])
            else:
                break;
        answer += 1
        
    return answer