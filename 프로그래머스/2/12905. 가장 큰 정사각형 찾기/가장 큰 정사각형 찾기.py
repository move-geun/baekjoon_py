def solution(board):
    answer = 0
    
    if len(board) == 1 or len(board[0]) == 1:
        return 1
    
    for i in range(1,len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j])+1
                answer = max(answer, board[i][j])
    
    return answer**2