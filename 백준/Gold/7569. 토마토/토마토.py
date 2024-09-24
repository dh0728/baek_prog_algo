from collections import deque
import sys
input = sys.stdin.readline

# 방향 벡터 (위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
dxyz = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

# 입력 받기
M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 큐 초기화 및 익은 토마토 좌표 모두 큐에 넣기
q = deque()
total_tomatoes = 0
ripe_tomatoes = 0

for z in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[z][i][j] == 1:  # 익은 토마토
                q.append((z, i, j, 0))
                ripe_tomatoes += 1
            if tomato[z][i][j] != -1:  # 토마토가 있는 칸이면
                total_tomatoes += 1

# BFS 수행
max_days = 0
while q:
    z, x, y, days = q.popleft()
    max_days = days  # 마지막에 저장된 day가 최대일
    for dz, dx, dy in dxyz:
        nz, nx, ny = z + dz, x + dx, y + dy
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomato[nz][nx][ny] == 0:
            tomato[nz][nx][ny] = 1  # 익음
            q.append((nz, nx, ny, days + 1))
            ripe_tomatoes += 1

# 결과 출력
if total_tomatoes == ripe_tomatoes:  # 모든 토마토가 익었다면
    print(max_days)
else:
    print(-1)