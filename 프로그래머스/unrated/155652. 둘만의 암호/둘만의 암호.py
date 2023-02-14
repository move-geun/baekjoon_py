def solution(s, skip, index):
    answer = ''
    base = [ _ for _ in range(97,123)]
    for i in skip:                          # 배열에서 skip 문자 지우기
        base.remove(ord(i))
        
    for i in s:                             # base에서 s 각 문자 검사  
        for b in range(0, len(base)):
            if ord(i) == base[b]:           # 같은걸 찾았으면 index 더해서 반환하기
                if b+index > len(base)-1:   # index 더한 범위가 z를 넘을 때 a로 되돌리기
                    tmp = (b + index) % len(base)
                    answer += chr(base[tmp])
                else:                       # 아니면 반환
                    answer += chr(base[b+index])
    return answer