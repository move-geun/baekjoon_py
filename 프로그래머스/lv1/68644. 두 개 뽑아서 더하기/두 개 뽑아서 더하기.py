from itertools import combinations

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in combinations(numbers, 2):
        answer.add(sum(i))
    return sorted(answer)
                  
# itertools 사용
# def solution(numbers):
#     answer = []
#     for i in combinations(numbers, 2):
#         answer.append(sum(i))
#     answer = list(set(answer))
#     return answer

# def solution(numbers):
#     answer = []
#     numbers.sort()
#     for i in range(0,len(numbers)):
#         for j in range(i+1,len(numbers)):
#             answer.append(numbers[i]+numbers[j])
#     answer = list(set(answer))
#     answer.sort()
#     return answer