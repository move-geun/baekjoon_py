lst = [-1]*26
words = list(map(str, input()))

for i in range(len(words)):
    idx = ord(words[i])-97
    if lst[idx] == -1:
        lst[idx] = i
print(*lst)