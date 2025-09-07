import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


MONKEY = [[0,1], [1,0], [0, -1], [-1, 0]]

HORSE = [ 
           [2, 1] ,[2, -1],
           [1, 2] ,[-1, 2],
           [-2, 1] ,[-2, -1],
           [1, -2] ,[ -1, -2]
        ]

K = int(input())
W, H = map(int, input().split())

board = []
for _ in range(H):
    board.append( list(map(int, input().split())))

def bfs(x,y):
    visited = [[-1] * W  for _ in range(H)]
    dq = deque([(x, y, K, 0)])
    visited[x][y] = True

    while dq:
        x, y, k, cnt = dq.popleft()

        if x == H - 1 and y == W - 1: # 도착했으면
            return cnt 
        
        # 원숭이 방식대로 이동할 경우
        for i, j in MONKEY:
            nx = x + i
            ny = y + j
            if nx < 0 or nx >= H or ny < 0 or ny >= W or visited[nx][ny] >= k or board[nx][ny]: # 판을 벗어나거나, 방문한 적이 있거나, 장애물이면
                continue

            visited[nx][ny] = k
            dq.append([nx, ny, k, cnt + 1])
        
        # 말처럼 이동할 경우
        
        if k:
            nk = k - 1
            for i, j in HORSE:
                nx = x + i
                ny = y + j
                if nx < 0 or nx >= H or ny < 0 or ny >= W or visited[nx][ny] >= nk or board[nx][ny]: # 판을 벗어나거나, 방문한 적이 있거나, 장애물이면
                    continue
                
                visited[nx][ny] = nk
                dq.append([nx, ny, nk, cnt + 1])
    
    return -1

def solution():

    answer = bfs(0,0)

    print(answer)

if __name__ == "__main__":
    solution()


