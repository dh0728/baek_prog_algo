
# 입력
N = int(input())
room = []
for i in range(N):
    room.append(input())

# 가로로 누울 자리 수
width = 0
for i in range(N):
    space = 0   # 누울 자리 공간
    for j in range(N):
        if room[i][j] == ".":
            space += 1
            if space == 2:
                width += 1
        else:
            space = 0
            continue

# 세로로 눈울 자리 수
length = 0
for i in range(N):
    space = 0   # 누울 자리 공간
    for j in range(N):
        if room[j][i] == ".":
            space += 1
            if space == 2:
                length += 1
        else:
            space = 0
            continue

# 출력
print(width, length)