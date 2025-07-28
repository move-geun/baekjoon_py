def solution(number, k):
    nums = list(map(int, number))
    stack = []
    cnt = 0
    answer = ''
    idx = 1
    stack.append(nums[0])
    while True:
        if cnt >= k or idx >= len(nums):
            break
        if stack:
            tmp = stack.pop()
            if tmp >= nums[idx]:
                stack.append(tmp)
                stack.append(nums[idx])
                idx += 1
            else:
                cnt += 1
        else:
            stack.append(nums[idx])
            idx += 1
    
    for i in nums[idx:]:
        stack.append(i)
    
    if cnt < k:
        for i in stack[:cnt-k]:
            answer += str(i)
    else:
        for i in stack:
            answer += str(i)

    return answer