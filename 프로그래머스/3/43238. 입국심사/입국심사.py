def solution(n, times):
    times.sort()
    l, r = 1, n * times[-1]
    answer = r

    while l <= r:
        mid = (l + r) // 2
        total = sum(mid // t for t in times)

        if total >= n:  # n명 이상 처리 가능
            answer = mid
            r = mid - 1
        else:           # n명 미만이면 시간 늘려야 함
            l = mid + 1

    return answer
