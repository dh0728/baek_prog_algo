import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input().strip())

dxy = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

def bfs(Sr, Sc, Fr, Fc):
    visited = [[False] * L for _ in range(L)]
    dq = deque([(Sr, Sc, 0)])
    visited[Sr][Sc] = True

    while dq:
        r, c, cnt = dq.popleft()

        if r == Fr and c == Fc:
            return cnt
        
        for dx, dy in dxy:
            nr = r + dx
            nc = c + dy
            if nr < 0 or nr >= L or nc < 0 or nc >= L: # 체스판을 벗어날 경우
                continue
            
            if visited[nr][nc]: # 이미 방문한 경우 
                continue
            visited[nr][nc] = True
            dq.append((nr, nc, cnt+1))

    return 0
    
for _ in range(T):
    L = int(input().strip())
    board = [[0] * L for _ in range(L)]
    Sr, Sc = map(int, input().split())
    Fr, Fc = map(int, input().split())
    print(bfs(Sr, Sc, Fr, Fc))
