# def solution(s):
#     tmp = s.replace('()', '')
#     while tmp:
#         if tmp[0] == ')':
#             return False
#         elif '()' not in tmp:
#             return False
#         tmp = tmp.replace('()', '')
    
#     return True

def solution(s):
    stack = []
    for c in s:
        if c=='(':
            stack.append(c)
        elif not stack or stack.pop()!='(':
                return False
    return False if stack else True