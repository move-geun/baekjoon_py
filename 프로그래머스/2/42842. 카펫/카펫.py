def solution(brown, yellow):
    total = brown + yellow
    tmp = []
    for i in range(1, yellow+1):
        if yellow%i == 0:
            tmp.append([i, int(yellow//i)])
    for i,j in tmp:
        ti,tj = i+2, j+2
        if ti*tj == total:
            if ti < tj:
                return [tj, ti]
            else: return [ti, tj]
