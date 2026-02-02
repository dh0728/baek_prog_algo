import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split()) 
board = [[0]*(M+1)]
for _ in range(N): 
    board.append([0] +list(map(int, input().split())))

dxy = [[0,1],[1,0],[0,-1],[-1,0]]
ps = [[0]*(M + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        ps[i][j] = (
            board[i][j]
            + ps[i-1][j]
            + ps[i][j-1]
            - ps[i-1][j-1]
        )

# H, W = 직사각형 크기
# Sr, Sc = 시작좌표 
# Fr, Fc = 도착좌표
H, W, Sr, Sc, Fr, Fc = map(int, input().split()) 

def can_move(r,c):
    r2 = r + H -1
    c2 = c + W -1

    if r2 > N or c2 > M:
        return True
    
    area = (
        ps[r2][c2]
        - ps[r-1][c2]
        - ps[r2][c-1]
        + ps[r-1][c-1]
    )
    return area != 0

visited = [[False]*(M+1) for _ in range(N+1)]

def bfs(r, c):

    visited[r][c] = 1
    dq = deque([(r,c,0)]) # 현재 위치 r, c, 이동횟수

    while dq:
        x, y, cnt = dq.popleft()

        if x == Fr and y == Fc:
            return cnt
        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx <= 0 or nx > N or ny <= 0 or ny > M:  # 범위를 벗어나면
                continue
            if visited[nx][ny]: # 이미 방문한적 있으면
                continue
                
            if can_move(nx, ny):
                continue
            
            visited[nx][ny] = True
            dq.append((nx, ny, cnt+1))
    return -1

def solution():

    res =bfs(Sr,Sc)
    print(res)

    
if __name__ == "__main__":
    solution()