def find_x_y(control):
    # 방향: 0=북, 1=동, 2=남, 3=서
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y = 0, 0  # 시작 좌표
    angle = 0  # 시작 방향: 북쪽
    
    # 최소/최대 좌표 저장 변수
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0
    
    for c in control:
        if c == 'L':
            angle = (angle - 1) % 4
        elif c == 'R':
            angle = (angle + 1) % 4
        elif c == 'F':  # 앞으로 이동
            x += dxy[angle][0]
            y += dxy[angle][1]
        else:  # 'B' 뒤로 이동
            x -= dxy[angle][0]
            y -= dxy[angle][1]
        
        # 이동 후 최소/최대 좌표 갱신
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    # 최종 직사각형의 넓이 계산
    return (max_x - min_x) * (max_y - min_y)

# 입력 처리 및 출력
T = int(input())
for _ in range(T):
    control_list = input().strip()
    result = find_x_y(control_list)
    print(result)