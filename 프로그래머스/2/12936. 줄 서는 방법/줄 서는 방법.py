def solution(n, k):
    people = list(range(1, n + 1))
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i

    k -= 1

    ans = []
    for i in range(n, 0, -1):
        idx = k // fact[i - 1]     
        k %= fact[i - 1]          
        ans.append(people.pop(idx))  

    return ans
