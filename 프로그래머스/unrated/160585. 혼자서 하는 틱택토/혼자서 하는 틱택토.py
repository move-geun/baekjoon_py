# 빙고 찾기
def tictacto(base):
    tic_O = tic_X = 0

    for i in range(0,3):
        # row check
        if base[i][0] == base[i][1] == base[i][2]:
            if base[i][0] == 'O':
                tic_O += 1
            elif base[i][0] == 'X':
                tic_X += 1
        # col check
        if base[0][i] == base[1][i] == base[2][i]:
            if base[0][i] == 'O':
                tic_O += 1
            elif base[0][i] == 'X':
                tic_X += 1
            
    # diagonal check
    if base[0][0] == base[1][1] == base[2][2]:
        if base[0][0] == 'O':
            tic_O += 1
        elif base[0][0] == 'X':
            tic_X += 1

    if base[0][2] == base[1][1] == base[2][0]:
        if base[0][2] == 'O':
            tic_O += 1
        elif base[0][2] == 'X':
            tic_X += 1

    return (tic_O,tic_X)


def solution(board):
    cnt_O = cnt_X = 0
    base = list()
    
    # 2차원 배열로 변경
    for i in board:
        base.append(list(i))
    
    # O와 X 갯수 찾기
    for i in range(0,3):
        for j in range(0,3):
            if base[i][j] == 'O':
                cnt_O += 1
            if base[i][j] == 'X':
                cnt_X += 1
    total = cnt_O + cnt_X
    
    # 일어날 수 없는 상황
    # 1. X가 많거나 O가 2개 이상 차이 날 때
    if cnt_O < cnt_X or cnt_O - 1 > cnt_X:
        return 0
    # 2. 빙고 체크
    tic_O, tic_X = tictacto(base)
    # 2-1. O를 마지막으로 게임 끝나는데
    if total >= 5 and total % 2:
        # X 빙고가 이미 있을 때
        if tic_X:
            return 0
    # 2-2. X를 마지막으로 게임 끝나는데
    if total >= 5 and not total % 2:
        # O 빙고가 이미 있을 때
        if tic_O:
            return 0

    return 1