def solution(phone_book):
    answer = True
    maps = {}
    for i in phone_book:
        maps[i] = 1
        
    for numbers in phone_book:
        tmp = ''
        for num in numbers:
            tmp += num
            
            if tmp in maps and tmp != numbers:
                return False
    return answer
