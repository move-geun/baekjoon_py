def solution(priorities, location):
    answer = 0
    target = [False for _ in range(len(priorities))]
    target[location] = True
    
    while True:
        # 0 인덱스 값이 가장 크고 target이라면
        if priorities[0] == max(priorities) and target[0]:
            answer += 1
            return answer
        # 0 인덱스 값이 가장 크지만 target은 아님
        elif priorities[0] == max(priorities):
            answer += 1
            del priorities[0]
            del target[0]
        # 그거 아니면
        else:
            priorities.append(priorities.pop(0))
            target.append(target.pop(0))
    return answer