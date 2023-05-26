def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(yellow,0,-1):
        if yellow%i==0:
            row, col = i, yellow//i
            if (row+2)*(col+2) == total:
                answer.append(row+2)
                answer.append(col+2)
                break
    return answer