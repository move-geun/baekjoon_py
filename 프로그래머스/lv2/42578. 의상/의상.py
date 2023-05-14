from collections import defaultdict

def solution(clothes):
    cloth_dict = defaultdict(int)
    for c in clothes:
        cloth_dict[c[1]] += 1 

    answer = 1
    for count in cloth_dict.values():
        answer *= (count+1)
    
    return answer - 1