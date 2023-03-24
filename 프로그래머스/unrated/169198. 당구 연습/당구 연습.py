def index(m, n, startX, startY, ball):
    tmp = 1000000
    # 위 대칭
    if tmp > ((startX-ball[0])**2 + (2*n-startY-ball[1])**2):
        tmp = (startX-ball[0])**2 + (2*n-startY-ball[1])**2
    # 아래 대칭
    if tmp > ((startX-ball[0])**2 + (-startY-ball[1])**2):
        tmp = (startX-ball[0])**2 + (-startY-ball[1])**2
    # 왼쪽 대칭
    if tmp > ((-startX-ball[0])**2 + (startY-ball[1])**2):
        tmp = (-startX-ball[0])**2 + (startY-ball[1])**2
    # 오른쪽 대칭
    if tmp > ((2*m-startX-ball[0])**2 + (startY-ball[1])**2):
        tmp = (2*m-startX-ball[0])**2 + (startY-ball[1])**2
    
    return tmp

def colIndex(m, n, startX, startY, ball):
    tmp = 1000000
    # 위 대칭
    if tmp > ((startX-ball[0])**2 + (2*n-startY-ball[1])**2):
        tmp = (startX-ball[0])**2 + (2*n-startY-ball[1])**2
    # 아래 대칭
    if tmp > ((startX-ball[0])**2 + (-startY-ball[1])**2):
        tmp = (startX-ball[0])**2 + (-startY-ball[1])**2
    # 벽치기
    if startX < ball[0]:
        if tmp > (startX + ball[0])**2:
            tmp = (startX + ball[0])**2
    if startX > ball[0]:
        if tmp > (2*m-startX-ball[0])**2:
            tmp = (2*m-startX-ball[0])**2
    
    return tmp

def rowIndex(m, n, startX, startY, ball):
    tmp = 1000000
    # 왼쪽 대칭
    if tmp > ((-startX-ball[0])**2 + (startY-ball[1])**2):
        tmp = (-startX-ball[0])**2 + (startY-ball[1])**2
    # 오른쪽 대칭
    if tmp > ((2*m-startX-ball[0])**2 + (startY-ball[1])**2):
        tmp = (2*m-startX-ball[0])**2 + (startY-ball[1])**2
    # 벽치기
    if startY < ball[1]:
        if tmp > (startY + ball[1])**2:
            tmp = (startY + ball[1])**2
    if startY > ball[1]:
        if tmp > (2*n-startY-ball[1])**2:
            tmp = (2*n-startY-ball[1])**2
    
    return tmp


def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        if startX == ball[0]:
            tmp = rowIndex(m, n, startX, startY, ball)
        elif startY == ball[1]:
            tmp = colIndex(m, n, startX, startY, ball)
        else:
            tmp = index(m, n, startX, startY, ball)
            
        answer.append(tmp)
    return answer