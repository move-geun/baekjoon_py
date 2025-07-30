def solution(nums):
    num = list(set(nums))
    print(len(nums)//2)
    return len(nums)//2 if len(nums)//2 < len(num) else len(num)