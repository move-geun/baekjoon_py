def solution(N, road, K):
    INF = 1e9
    dist = [[INF]*(N+1) for _ in range(N+1)]
    
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                dist[i][j] = 0
    
    for si,ei,val in road:
        dist[si][ei] = min(dist[si][ei], val)
        dist[ei][si] = min(dist[ei][si], val)
    
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if dist[i][k] != INF and dist[k][j]  != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return len([x for x in dist[1] if x <= K])