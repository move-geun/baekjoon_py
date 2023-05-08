def solution(targets):
    cnt = 0
    m_start = m_end = 0
    targets = sorted(targets, key=lambda t: (t[0], -t[1]))
    for t_start, t_end in targets:
        if m_start <= t_start < m_end or m_start <= t_end < m_end:
            m_start, m_end = sorted([m_start, m_end, t_start, t_end])[1: 3]
        else:
            cnt += 1
            m_start, m_end = t_start, t_end

    return cnt