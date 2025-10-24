def dfs(L,n,board):
    global cnt 
    if L == n:
        cnt+=1
    for i in range(n):
        for j in range(L):
            if board[j] == i:
                break
            if L-j == abs(i- board[j]):
                break
        else:
            board[L] = i
            dfs(L+1, n,board)
                

def solution(n):
    global cnt
    cnt = 0
    board = [-1]* n
    dfs(0,n,board)
    return cnt