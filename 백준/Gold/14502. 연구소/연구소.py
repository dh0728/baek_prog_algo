import sys
from collections import deque
import copy
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N, M= map(int, input().split())

dxy = [[0, 1],[1, 0],[0, -1],[-1, 0]]

board = [list(map(int, input().split())) for _ in range(N)]
empty = []
virus = []

safe_zone = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            safe_zone += 1
            empty.append((i,j))
        if board[i][j] == 2:
            virus.append((i,j))



def bfs(rc1, rc2, rc3, safe_zone):
    board_copy = copy.deepcopy(board)
    board_copy[rc1[0]][rc1[1]] = 1
    board_copy[rc2[0]][rc2[1]] = 1
    board_copy[rc3[0]][rc3[1]] = 1
    dq = deque()

    for v in virus:
        dq.append(v)

    while dq:
        r ,c = dq.popleft() 
        for dx, dy in dxy:

            nr = r + dx
            nc = c + dy

            # 범위를 벗어나면
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 벽이면 패스
            if board_copy[nr][nc] == 1:
                continue

            # 이미 바이러스가 퍼진 방이면 패스
            if board_copy[nr][nc] == 2:
                continue

            board_copy[nr][nc] = 2
            dq.append((nr, nc))


    cnt = 0
    for i in range(N):
        for j in range(M):
            if board_copy[i][j] == 0:
                cnt +=1
    
    return cnt



empty_size = len(empty)
res = 0
for i in range(0, empty_size - 2):
    for j in range(i+1, empty_size - 1):
        for k in range(j+1, empty_size):

            cnt = bfs(empty[i], empty[j], empty[k], safe_zone)
            if cnt > res:
                res = cnt

print(res)

'''
무식하게 다 찾아서 하는 방법
for i in range(N*M):
    r1 = i // M
    c1 = i % M
    for j in range(i+1, N*M):
        r2 = j // M
        c2 = j % M
        for k in range(j +1, N*M):
            r3 = k // M
            c3 = k % M
'''


