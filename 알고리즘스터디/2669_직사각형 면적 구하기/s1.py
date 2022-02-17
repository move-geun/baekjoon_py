
box_lists = list()

for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    
    # 빈 리스트에 넣고 
    for i in range(x2,x1,-1):
        for j in range(y2,y1,-1):
            box_lists.append((i,j))

    # 중복값 삭제하고 
    result = list(set(box_lists))

# 갯수 세기
print(len(result))
