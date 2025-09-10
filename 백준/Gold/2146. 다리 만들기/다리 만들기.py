import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N = int(input())

board = [ list(map(int, input().split())) for _ in range(N)]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

island = [[0] * N for _ in range(N)] # 섬 라벨링


def labeling_dfs(x, y, n):
    
    stack = [(x, y)]
    island[x][y] = n

    while stack:

        i , j = stack.pop()

        for dx, dy in dxy:
            nx = i + dx
            ny = j + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N or island[nx][ny] != 0 or board[nx][ny] == 0:
                continue

            island[nx][ny] = n
            stack.append((nx, ny))
    return

def labeling(): # 섬은 숫자 2부터 차례로 1 : 육지, 0: 바다라서

    label = 2
    for i in range(N):
        for j in range(N):
            if board[i][j] and island[i][j] == 0:
                labeling_dfs(i, j, label)
                label += 1

    


# 2) 멀티소스 BFS: 모든 육지(각 섬)를 거리0로 동시에 시작, 바다로만 퍼짐
def bfs():
    owner = [[-1]*N for _ in range(N)]  # 이 칸을 처음 점유한 섬 ID
    dist  = [[-1]*N for _ in range(N)]  # 바다에서 확장된 거리(육지는 0)
    q = deque()

    # 모든 육지를 초기 큐에 넣음 (거리0)
    for i in range(N):
        for j in range(N):
            if island[i][j] > 1:
                owner[i][j] = island[i][j]
                dist[i][j] = 0
                q.append((i, j))

    ans = 10**9

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if board[nx][ny] == 0:
                # 바다이면서 미점유 → 내 섬으로 확장
                if owner[nx][ny] == -1:
                    owner[nx][ny] = owner[x][y]
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                # 바다이지만 이미 다른 섬이 점유한 파동이면 만남 → 후보 길이 갱신
                elif owner[nx][ny] != owner[x][y]:
                    cand = dist[x][y] + dist[nx][ny]
                    if cand < ans:
                        ans = cand
            else:
                # 육지(다른 섬)와 바로 맞닿아 있을 수도 있으니 체크 (실제로는 발생 X: 4방이면 같은 섬)
                if owner[nx][ny] != -1 and owner[nx][ny] != owner[x][y]:
                    cand = dist[x][y] + dist[nx][ny]  # 육지 dist는 0
                    if cand < ans:
                        ans = cand

    return ans

def solution():

    labeling()

    answer = bfs()
    
    print(answer)


if __name__ == "__main__":
    solution()


