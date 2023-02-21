def solution(a, b, n):
    answer = n//a*b
    tmp = n%a + answer
    
    while tmp >= a:
        answer += tmp//a*b
        tmp = tmp%a + tmp//a*b
        
    return answer