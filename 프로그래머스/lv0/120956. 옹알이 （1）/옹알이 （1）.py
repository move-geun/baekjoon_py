def solution(babbling):
    answer = 0
    babb = ["aya","ye","woo","ma"]
    for ba in babbling:
        for i in babb:
            ba = ba.replace(i, '!',1)
        ba = ba.replace('!', '')
        if len(ba) == 0 :
            answer += 1
    return answer