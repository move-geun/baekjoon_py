def solution(numbers):
    str_numbers = list(map(str, numbers))
    tmp = sorted(str_numbers, key=lambda num: num*3, reverse=True)
    
    return str(int(''.join(tmp)))
