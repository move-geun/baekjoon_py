def solution(babbling):
    answer = 0
    can = ["aya","ye","woo","ma"]
    for bab in babbling:
        for i in can:
            if i*2 not in bab:
                bab = bab.replace(i," ")
        if bab.strip() == "":
            answer += 1
            
    return answer