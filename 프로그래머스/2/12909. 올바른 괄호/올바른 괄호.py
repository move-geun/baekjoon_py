def solution(s):
    stack = []
    for i in s:
        if len(stack)==0:
            stack.append(i)
        elif i == '(':
            stack.append('(')
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    
    return False if len(stack) else True