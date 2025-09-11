import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split()) # N : 가로, M : 세로

board = [ list(map(int, input().split())) for _ in range(M)]
rooms = [[0] * N for _ in range(M)]
dxy = [[0, -1],[-1, 0],[0, 1],[1, 0]] # 서 북 동 남

size_list = [0]

def wall_list(b):

    dirs = []
    if not b & 1:
        dirs.append(0)
    if not b & 2:
        dirs.append(1)
    if not b & 4:
        dirs.append(2)
    if not b & 8:
        dirs.append(3)

    return dirs

def room_labeling(i, j, num):
    cnt = 1
    q = deque()
    q.append([i, j])
    rooms[i][j] = num

    while q:

        x, y = q.popleft()
        dirs = wall_list(board[x][y]) 


        for k in dirs:
            nx = x + dxy[k][0]
            ny = y + dxy[k][1]

            if nx < 0 or nx >= M or ny < 0 or ny >= N or rooms[nx][ny] != 0: # 이미 방이거나 범위 벗어나면 패스
                continue

            rooms[nx][ny] = num
            q.append([nx, ny])
            cnt += 1

    return cnt

# 이웃한 방 찾기
def find_max_sum_size():

    max_sum_size = 0
    for i in range(M):
        for j in range(N):
            # 동(2), 남(3)만 보면 중복 없음
            for k in (2, 3):  # dxy 인덱스: 동, 남
                ni = i + dxy[k][0]
                nj = j + dxy[k][1]
                if 0 <= ni < M and 0 <= nj < N:
                    a = rooms[i][j]
                    b = rooms[ni][nj]
                    if a != b:
                        s = size_list[a] + size_list[b]
                        if s > max_sum_size:
                            max_sum_size = s

    return max_sum_size

    

    


def solution():

    room_num = 1
    max_room_size = 0
    max_sum_size = 0

    
    for i in range(M):
        for j in range(N):
            if rooms[i][j] == 0:
                room_size = room_labeling(i,j, room_num)
                room_num += 1
                size_list.append(room_size)

                if room_size > max_room_size:
                    max_room_size = room_size

    print(room_num - 1)
    print(max_room_size)

    max_sum_size = find_max_sum_size()
    
    print(max_sum_size)

if __name__ == "__main__":
    solution()
