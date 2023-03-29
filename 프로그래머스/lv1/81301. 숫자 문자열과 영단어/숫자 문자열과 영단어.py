def solution(s):
    # 임시문자열 받을 tmp
    tmp = ''
    answer = ''
    nums = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    
    for i in list(s):
        # 숫자면 문자로 바꿔서 answer 추가
        if i.isdigit():
            answer += i
        # 문자면 num 찾아서 answer 추가
        else:
            tmp += i
            if tmp in nums.keys():
                answer += nums[tmp]
                tmp = ''
    
    return int(answer)