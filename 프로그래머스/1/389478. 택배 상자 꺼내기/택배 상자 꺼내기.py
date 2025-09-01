def solution(n, w, num):
         
    floor = (num - 1) // w      # 0-based 층
    offset = (num - 1) % w      # 그 층에서 0-based 위치

    if floor % 2 == 0:          # 짝수층: 왼 -> 오
        st = offset + 1
    else:                       # 홀수층: 오 -> 왼
        st = w - offset

    next_box = num
    
    cnt = 1
    for i in range(n):
        if floor % 2 == 0: # 짝수층
            next_box += 2 * w - 2 * st + 1
        else:
            next_box += 2 * st - 1
        
        if next_box <= n: # 꺼내야 하는 박스 번호가 존재하면
            cnt += 1
            floor += 1
        else:
            break
    return cnt