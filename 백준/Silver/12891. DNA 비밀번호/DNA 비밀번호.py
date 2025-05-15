import sys
from collections import defaultdict

input = sys.stdin.readline

s,p = map(int, input().split(' '))
lst = list(input().strip())
cut_lst = ['A','C','G','T']
cut_cnt = list(map(int, input().split(' ')))
cut_dict = {}
tmp = lst[:p]
answer = 0
spell_cnt = defaultdict(int)
for i in range(4):
    cut_dict[cut_lst[i]] = cut_cnt[i]
    spell_cnt[cut_lst[i]] = 0
for i in tmp:
    spell_cnt[i] += 1

def check(a,b):
    # a가 최소 필요수 
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True

if check(list(cut_dict.values()), list(spell_cnt.values())):
    answer += 1

for ei in range(p, s):
    spell_cnt[lst[ei-p]] -= 1
    spell_cnt[lst[ei]] += 1

    if check(list(cut_dict.values()), list(spell_cnt.values())):
        answer += 1

print(answer)