def solution(x):
    # x를 문자열로 변환하고, 각 자릿수의 합을 구합니다.
    digit_sum = sum([int(digit) for digit in str(x)])
    
    # x가 자릿수의 합으로 나누어 떨어지면 True를 반환하고,
    # 그렇지 않으면 False를 반환합니다.
    return x % digit_sum == 0