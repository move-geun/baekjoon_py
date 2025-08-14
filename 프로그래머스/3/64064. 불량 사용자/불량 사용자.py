from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    candi = [[] for _ in range(len(banned_id))]
    
    def isTrue(astr,bstr):
        if len(astr) == len(bstr):
            for i in range(len(astr)):
                if bstr[i] == '*':
                    continue
                elif astr[i] != bstr[i]:
                    return False
            return True
        else:
            return False
    
    for i in range(len(banned_id)):
        for user in user_id:
            if isTrue(user, banned_id[i]):
                candi[i].append(user)
    
    result = set()

    def dfs(i, used):
        if i == len(candi):
            result.add(frozenset(used))
            return
        for uid in candi[i]:
            if uid not in used:
                dfs(i + 1, used + [uid])

    dfs(0, [])
    
    return len(result)