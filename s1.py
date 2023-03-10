# 빙고 찾기
def tictacto(base,x,y,check,player):
    if check == 3:
        return True

    else:
        dx = [-1,-1,0,1,1,1,0,-1]
        dy = [0,1,1,1,0,-1,-1,-1]

        for i in range(0,8):
            ni = x + dx[i]
            nj = y + dy[i]

            if 0 <= ni <= 2 and 0 <= nj <= 2 and base[ni][nj] == player:
                tictacto(base,ni,nj,check+1,player)
            else:
                break
    return False


def solution(board):
    answer = -1
    cnt_O = cnt_X = 0
    x_list = list()
    base = list()
    
    # 2차원 배열로 변경
    for i in board:
        base.append(list(i))
    
    # O와 X 갯수 찾기
    for i in range(0,3):
        for j in range(0,3):
            if base[i][j] == 'O':
                cnt_o += 1
            if base[i][j] == 'X':
                cnt_x += 1
                x_list.append((i,j))
    
    # 일어날 수 없는 상황
    # 1. x가 더 많은 경우
    if cnt_x > cnt_o:
        answer =  0
    # 2. x가 3인데 o가 빙고
    elif cnt_x >= 3:
        tictacto(base,)
        
    # 3. x가 4인데 x가 빙고
        
    
    
    return answer