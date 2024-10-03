import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(s, e):
    global min_cnt
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # 2차원 배열을 벽을 부순 상태와 아닌 상태로 구분

    q = deque()
    q.append([s, e, 1, 1])  # x, y, 칸 수, 벽을 부술 수 있는 횟수
    visited[s][e][1] = 1  # 시작 위치에서 벽을 부수지 않은 상태로 방문 처리

    while q:
        x, y, cnt, block = q.popleft()

        # 목표 지점 도착하면 최소 경로 갱신
        if x == N - 1 and y == M - 1:
            min_cnt = min(min_cnt, cnt)
            continue

        for dx, dy in dxy:
            ni = x + dx
            nj = y + dy

            if ni < 0 or ni >= N or nj < 0 or nj >= M:  # 경로가 범위를 벗어나면 패스
                continue

            # 벽을 부수지 않고 이동할 수 있는 경우
            if maps[ni][nj] == 0 and visited[ni][nj][block] == 0:
                visited[ni][nj][block] = 1
                q.append([ni, nj, cnt + 1, block])

            # 벽을 부수고 이동해야 하는 경우
            elif maps[ni][nj] == 1 and block == 1 and visited[ni][nj][0] == 0:
                visited[ni][nj][0] = 1
                q.append([ni, nj, cnt + 1, 0])

    return

N, M = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]
min_cnt = N * M + 1  # 최단 경로를 초기화할 때 충분히 큰 값으로 설정

bfs(0, 0)

# 결과 출력
if min_cnt == N * M + 1:
    print(-1)
else:
    print(min_cnt)