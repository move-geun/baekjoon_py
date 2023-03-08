def solution(k, score):
    answer = []
    tmp = []
    for i in score:
        if len(tmp) < k:
            tmp.append(i)
            tmp.sort(reverse=True)
        else:
            tmp.append(i)
            tmp.sort(reverse=True)
            del tmp[-1]
        answer.append(tmp[-1])

    return answer