import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split()) 
dxy = [[0,1],[1,0],[0,-1],[-1,0]]
dist = [[INF] * N for _ in range(M)]
Fr = M-1
Fc = N-1

board = [list(map(int, input().strip())) for _ in range(M)]

def bfs(Sr, Sc, Fr, Fc):
    visited = [[False] * N for _ in range(M)]
    dq = deque([(Sr, Sc, 0)])
    visited[Sr][Sc] = True

    while dq:
        r, c, aoj = dq.popleft()

        if r == Fr and c == Fc:
            return dist[r][c]
        
        for dx, dy in dxy:
            nx = r + dx
            ny = c + dy

            # 범위를 벗어나면 패스
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            if board[nx][ny] == 0:
                dist[nx][ny] = min(dist[nx][ny], aoj)
                dq.appendleft((nx, ny, dist[nx][ny]))
            else:
                dist[nx][ny] = min(dist[nx][ny], aoj +1)
                dq.append((nx, ny, dist[nx][ny]))
            visited[nx][ny] = True
            
    return -1

if Fr == 0 and Fc == 0:
    print(0)
else:
    bfs(0,0,M-1,N-1)
    print(dist[M-1][N-1])