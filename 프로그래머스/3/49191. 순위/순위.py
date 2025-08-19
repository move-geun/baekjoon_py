def solution(n, results):
    answer = 0
    INF = 1e9
    dist = [[0]*(n+1) for _ in range(n+1)]
    
    for si,ei in results:
        dist[si][ei] = 1
        dist[ei][si] = -1
    
    for k in range(1,n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] == 1 and dist[k][j] == 1:
                    dist[i][j] = 1
                    dist[j][i] = -1
                elif dist[i][k] == -1 and dist[k][j] == -1:
                    dist[i][j] = -1
                    dist[j][i] = 1
    
    for dis in dist[1:]:
        if len([x for x in dis if x == 0]) == 2:
            answer += 1
    return answer