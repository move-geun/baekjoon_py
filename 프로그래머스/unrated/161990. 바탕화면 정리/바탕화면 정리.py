def solution(wallpaper):
    answer = []
    # tmp_left = len(wallpaper[0]) + 1
    # tmp_top = len(wallpaper) + 1
    # tmp_right = tmp_bottom = 0
    
    # for i in range(0, len(wallpaper)):
    #     for j in range(0, len(wallpaper[i])):
    #         if wallpaper[i][j] == '#':
    #             if i < tmp_top:
    #                 tmp_top = i
    #             if j < tmp_left:
    #                 tmp_left = j
    #             if i > tmp_bottom:
    #                 tmp_bottom = i
    #             if j > tmp_right:
    #                 tmp_right = tmp_right
    # answer.append(tmp_left)
    # answer.append(tmp_top)
    # answer.append(tmp_bottom + 1)
    # answer.append(tmp_right + 1)
    
    tmp_map = list()
    for i in range(0, len(wallpaper)):
        for j in range(0, len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                tmp_map.append((i,j))

    answer.append(min(tmp_map)[0])
    answer.append(min(tmp_map, key = lambda a: a[1])[1])
    answer.append(max(tmp_map)[0]+1)
    answer.append(max(tmp_map, key = lambda a: a[1])[1]+1)
    
    return answer