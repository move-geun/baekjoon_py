def solution(wallet, bill):
    answer = 0
    while True:
        if (bill[0] <= wallet[0] and bill[1] <= wallet[1]) or (bill[1] <= wallet[0] and bill[0] <= wallet[1]):
            break

        bill = [bill[0]//2, bill[1]] if bill[0] > bill[1] else [bill[0], bill[1]//2]
        answer += 1
    return answer