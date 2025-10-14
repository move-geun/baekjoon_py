def solution(sequence, k):
    n = len(sequence)
    li = ri = 0
    s = sequence[0]
    ans = []

    while li <= ri and ri < n:
        if s == k:
            ans.append([li, ri, ri - li])
            # 진행을 위해 왼쪽을 줄임
            s -= sequence[li]
            li += 1
        elif s < k:
            ri += 1
            if ri == n:
                break
            s += sequence[ri]
        else:  # s > k
            s -= sequence[li]
            li += 1
            # li가 ri를 넘어가면 창을 리셋
            if li > ri and li < n:
                ri = li
                s = sequence[li]
    ans.sort(key = lambda x : x[2])

    return [ans[0][0],ans[0][1]]
