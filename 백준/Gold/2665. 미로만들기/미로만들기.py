import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

dxy = [[0,1],[1,0],[0,-1],[-1,0]]

N = int(input().strip())
board = [list(map(int, input().strip())) for _ in range(N)] # 0: 벽 1: 흰방 


def solution(sr,sc, er, ec):
    dist = [[INF] * N for _ in range(N)]
    dq = deque([(sr, sc, 0)])
    dist[sr][sc] = 0

    while dq:
        r,c,cnt = dq.popleft()

        # 목적지 도착하면
        if r == er and c == ec:
            if dist[r][c] > cnt:
                dist[r][c] = cnt
            continue
        
        for dx , dy in dxy:
            nr = r + dx
            nc = c + dy

            # 범위를 벗어나면
            if nr < 0 or nr >= N or nc < 0 or nc >= N: 
                continue
            
            next_cnt = cnt
            # 검은 방이면
            if board[nr][nc] == 0:
                next_cnt = cnt + 1

            # 최소 경로를 찾으면
            if dist[nr][nc] > next_cnt:
                dist[nr][nc] = next_cnt
                dq.append((nr,nc,next_cnt))
    
    return dist[er][ec]

res = solution(0,0,N-1,N-1)
print(res)