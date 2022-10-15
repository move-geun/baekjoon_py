math = input()
aws = i = 0
flag = False
first = True
tmp = ''
while i <= len(math):
    if i == len(math):
        if flag :
            aws -= int(tmp)
        else:
            aws += int(tmp)
        break
    
    if first :
        if math[i] == '-':
            flag = True
            i += 1
            if tmp :
                aws += int(tmp)
                tmp = ''
                first = False

    if math[i] == '-' or math[i] == '+':
        if math[i] == '-':
            flag = True
        if flag :
            aws -= int(tmp)
            tmp = ''
            i += 1
        else:
            aws += int(tmp)
            tmp = ''
            i += 1 
    else:
        tmp += math[i]
        i += 1
print(aws)
