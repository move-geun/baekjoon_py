import math

def find_largest_proper_divisor(n):
    if n == 1:
        return 0
    
    answer = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if 10000000 < int(n / i):
                answer = max(answer, i)
            else:
                answer = max(answer, int(n/i))
    
    return answer

def solution(begin, end):
    answer = []
    
    while begin <= end:
        answer.append(find_largest_proper_divisor(begin))
        begin += 1
        
    return answer