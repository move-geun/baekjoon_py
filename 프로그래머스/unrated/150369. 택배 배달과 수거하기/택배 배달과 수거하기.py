def solution(cap, n, deliveries, pickups):
    answer = 0
    del_cnt = 0
    pick_cnt = 0

    for i in range(n):
		# 마지막 배달지부터 합해준다
        del_cnt += deliveries[n-i-1]
        pick_cnt += pickups[n-i-1]
				
		# 만약 배달이나 픽업 할 건수가 있다면
        while del_cnt > 0 or pick_cnt > 0:
			# 거리에 추가해준다
            answer += n-i
			# 남는 공간만큼 빼준다 (다른 배달지에 배송/픽업한것과 동일)
            del_cnt -= cap
            pick_cnt -= cap

    return answer*2