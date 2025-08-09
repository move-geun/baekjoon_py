from itertools import permutations

def solution(word):
    answer = 0
    tmp = ['A','A','A','A','A', 'E','E','E','E','E', 'I','I','I','I','I', 'O','O','O','O','O', 'U','U','U','U','U']
    ttmp = []
    for i in range(1,6):
        tttmp = list(permutations(tmp, i))
        a = list(set(tttmp))
        for j in a:
            ttmp.append(''.join(j))

    ttmp.sort()

    return ttmp.index(word)+1