bases = list()
while True:
    tmp = input()
    bases.append(tmp)
    if tmp == '.':
        break

for base in bases:
    if base == '.':
        break
    No = False
    stack = list()
    for i in base:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] =='[':
                No = True
                break
            else :
                del stack[-1]
        elif i == ']':
            if len(stack) == 0 or stack[-1] == '(':
                No = True
                break
            else:
                del stack[-1]
    
    if No :
        print('no')
    else:
        if len(stack) == 0 :
            print('yes')
        else:
            print('no')


