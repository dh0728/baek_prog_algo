import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

M = 12
N = 6

board =[list(input().strip()) for _ in range(12)]

dxy = [[0, 1],[1, 0],[0, -1],[-1, 0]]

# 빈공간을 메우는 메서드
def drop_alpa():
    for j in range(N):
        stack = []

        for i in range(M -1, -1, -1):
            if board[i][j] != '.':
                stack.append(board[i][j])

        r = M - 1
        for s in stack:
            board[r][j] = s
            r -=1
        
        for i in range(r+1):
            board[i][j] = '.'

## 연쇄가 일어날 수 있는지 확인
def bfs_group(sr, sc, v):

    color = board[sr][sc]

    q = deque([(sr, sc)])

    v[sr][sc] = True
    puyos = [(sr, sc)]
    while q:

        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N or v[nx][ny] or board[nx][ny] != color:
                continue
            
            v[nx][ny] = True
            q.append([nx, ny])
            puyos.append((nx,ny))

    return puyos
 
def solution():
    
    result = 0

    while True:

        v = [[False] * N for _ in range(M)]
        to_pop = set()

        for i in range(M):
            for j in range(N):
                if board[i][j] == '.' or v[i][j]:
                    continue
                
                puyos = bfs_group(i, j, v)
                if len(puyos) >= 4:
                    to_pop.update(puyos)
        
        if not to_pop:
            break

        for x, y in to_pop:
            board[x][y] = '.'

        drop_alpa()
        result += 1

    print(result)


if __name__ == "__main__":
    solution()


