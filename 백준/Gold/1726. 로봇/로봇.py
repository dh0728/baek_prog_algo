import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


M, N = map(int, input().split())  # 세로 M, 가로 N

dxy = [0, [0, 1],[1,0],[0, -1],[-1, 0]]

board = [ list(map(int, input().split())) for _ in range(M)]


# 바로보는 방향 : 동쪽 = 1, 서쪽 = 2, 남쪽 = 3, 북쪽 = 4
# 출발 지점의 위치
start = list(map(int, input().split())) # 행 , 열, 바라보는 방향

# 바로보는 방향 : 동쪽 = 1, 남쪽 = 2, 서쪽 = 3, 북쪽 = 4 으로 시계방향으로 변경
if start[2] == 2:
    start[2] = 3
elif start[2] == 3:
    start[2] = 2


# 도작 지점의 위치
end = list(map(int, input().split())) # 행, 열, 바라보는 방향


# 바로보는 방향 : 동쪽 = 1, 남쪽 = 2, 서쪽 = 3, 북쪽 = 4 으로 시계방향으로 변경
if end[2] == 2:
    end[2] = 3
elif end[2] == 3:
    end[2] = 2

start[0] -= 1 
start[1] -= 1
end[0] -= 1 
end[1] -= 1


def turning_counting(dir1, dir2):

    n = abs(dir1 - dir2)

    if n == 0:
        return 0

    if n % 2 == 1: # 홀수이면 1칸
        return 1
    else: 
        return 2

def bfs():
    
    visited = [[[-1]*5 for _ in range(N)] for _ in range(M)]
    q = deque()

    sx, sy, sd = start
    ex, ey, ed = end

    visited[sx][sy][sd] = 0
    q.append([sx, sy, sd])

    def right(d):  # 시계 회전
        return 1 if d == 4 else d + 1
    def left(d):   # 반시계 회전
        return 4 if d == 1 else d - 1

    while q:
        x, y, dir = q.popleft()
        cur = visited[x][y][dir]

        # 목표 상태(좌표+방향)에 도달하면 종료
        if x == ex and y == ey and dir == ed:
            return cur

        # 1) Turn left / right (각 1명령)
        for nd in (left(dir), right(dir)):
            if visited[x][y][nd] == -1:
                visited[x][y][nd] = cur + 1
                q.append([x, y, nd])

        # 2) Go k (k=1..3) — 중간 칸이 막히면 더 멀리는 불가 → break
        dx, dy = dxy[dir]
        for k in (1, 2, 3):
            nx = x + dx * k
            ny = y + dy * k
            if not (0 <= nx < M and 0 <= ny < N):  # 범위 밖
                break
            if board[nx][ny] == 1:                 # 장애물
                break
            if visited[nx][ny][dir] == -1:
                visited[nx][ny][dir] = cur + 1
                q.append([nx, ny, dir])

    # 문제에서 "항상 이동 가능"이라 여기 안 옴. 안전하게 -1 반환
    return -1

def solution():

    result =bfs()

    print(result)

if __name__ == "__main__":
    solution()


