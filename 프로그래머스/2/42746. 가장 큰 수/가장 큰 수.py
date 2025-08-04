def solution(numbers):
    answer = ''
    lst = [str(i) for i in numbers]
    tmp = sorted(lst, key = lambda x : x*4, reverse=True)
    ttmp = ''.join(tmp)
    return '0' if ttmp[0] == '0' else ttmp


