from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_count = defaultdict(int) # 각 사용자에 대해 신고를 받은 횟수
    user_reports = defaultdict(set) # 각 사용자가 신고한 대상
    for r in report:
        user_from, user_to = r.split()
        if user_to not in user_reports[user_from]: # 중복 신고 방지
            report_count[user_to] += 1
        user_reports[user_from].add(user_to)

    banned = {key for key, value in report_count.items() if value >= k}
    # 정지 대상이 누구인지 미리 구하기
    mail_targets = defaultdict(set)
    for user, reports in user_reports.items():
        targets = reports & banned
        for target in targets:
            mail_targets[target].add(user)

    # 정지 대상에게 메일 보내기
    for user, targets in mail_targets.items():
        for target in targets:
            answer[id_list.index(target)] += 1

    return answer