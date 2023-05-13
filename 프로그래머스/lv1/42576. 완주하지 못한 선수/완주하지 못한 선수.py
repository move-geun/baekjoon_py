import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# from collections import defaultdict

# def solution(participant, completion):
#     answer = ''
#     finish = defaultdict(int)
#     for i in participant:
#         finish[i] += 1
#     for i in completion:
#         finish[i] -= 1
#     for i in finish:
#         if finish[i] >= 1:
#             answer += i
        
#     return answer