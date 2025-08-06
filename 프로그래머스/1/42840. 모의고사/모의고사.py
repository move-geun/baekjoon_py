def solution(answers):
    answer = []
    nums = {'one':[1,2,3,4,5], 'two':[2,1,2,3,2,4,2,5], 'three':[3,3,1,1,2,2,4,4,5,5]}
    ans = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if answers[i] == nums["one"][i%5]:
            ans[1] += 1
        if answers[i] == nums["two"][i%8]:
            ans[2] += 1
        if answers[i] == nums["three"][i%10]:
            ans[3] += 1
    answer = [k for k,v in ans.items() if max(ans.values()) == v]
    return answer