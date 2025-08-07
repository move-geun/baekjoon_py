from itertools import permutations

def isPrime(nums):
    for i in range(2, int(nums**0.5)+1):
        if nums%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = list(numbers)
    sets = set()
    for i in range(1,len(nums)+1):
        tmp = list(permutations(nums, i))
        for t in tmp:
            sets.add(t)
    set_list = list(sets)
    set_nums = list(set(int(''.join(x)) for x in set_list))
    for i in set_nums:
        if i <2:
            continue
        else:
            answer += isPrime(i)
    return answer