def solution(sizes):
    max_w, max_h = 0, 0
    for w,h in sizes:
        if h>w:
            if max_w < h :
                max_w = h
            if max_h < w:
                max_h = w
        else:
            if max_w < w:
                max_w = w
            if max_h < h:
                max_h = h
        
    return max_w*max_h