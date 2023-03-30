def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    candi = 0
    tmp = 0
    for lo in lottos:
        if lo == 0:
            candi += 1
        elif lo in win_nums:
            tmp += 1
    
    answer.append(rank[tmp])
    answer.append(rank[tmp+candi])
    answer.sort()
    
    return answer