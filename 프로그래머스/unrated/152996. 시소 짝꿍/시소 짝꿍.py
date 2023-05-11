from collections import defaultdict

def solution(weights):
    answer = 0
    info = defaultdict(int)
    
    for w in weights:
        # 지금 무게와 짝이 되는 무게 있는지 확인, 없으면 등록
        answer += info[w] + info[w*2] + info[w/2] + info[(w*2)/3] + info[(w*3)/2] + info[(w*4)/3] + info[(w*3)/4]
        # 지금 무게 추가
        info[w] += 1

    return answer