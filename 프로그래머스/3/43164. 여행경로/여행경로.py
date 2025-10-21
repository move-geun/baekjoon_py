from collections import defaultdict

def solution(tickets):
    answer = []
    t = defaultdict(list)
    
    for a,b in tickets:
        t[a].append(b)
    
    for ta in t:
        t[ta].sort(reverse=True)
    
    stack = ["ICN"]
    while stack:
        cur = stack[-1]
        if t[cur]:
            stack.append(t[cur].pop())
        else:
            answer.append(stack.pop())

    return answer[::-1]