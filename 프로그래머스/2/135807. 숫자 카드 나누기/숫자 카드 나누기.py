def solution(arrayA, arrayB):
    answer = 0
    def gcd(a,b):
        r = a%b
        if r==0:
            return b
        return gcd(b,r)
    
    def cd(a):
        lst = []
        for i in range(1, a+1):
            if a%i==0:
                lst.append(i)
        return lst[1:]
    
    idx = 1
    a = arrayA[0]
    b = arrayB[0]
    
    while idx < len(arrayA):
        a = gcd(a, arrayA[idx])
        b = gcd(b, arrayB[idx])
        idx+=1
    
    acd = cd(a)
    bcd = cd(b)
    acd.sort(reverse=True)
    bcd.sort(reverse=True)
    
    if acd:
        for i in acd:
            for b in arrayB:
                if b%i==0:
                    break
            else:
                answer = max(i, answer)
    if bcd:
        for j in bcd:
            for a in arrayA:
                if a%j==0:
                    break
            else:
                answer = max(j, answer)
    return answer