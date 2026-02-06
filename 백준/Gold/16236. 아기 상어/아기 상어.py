import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]
dxy = [[-1,0],[0,-1],[0,1],[1,0]] # 순서 중요 상왼오하 

def find_shark():
    for i in range(N):
      for j in range(N):
        if board[i][j] == 9:
            r = i
            c = j
            return r, c    

def bfs(r,c):
    visited = [[False] * N for _ in range(N)] 
    dq = deque([(r,c,0)])
    visited[r][c] = True

    fish = []
    min_dist = INF

    while dq:
        x, y, dist = dq.popleft() 

        if dist > min_dist: # 이미 더 먼 거리면 종료
            break
        
        if board[x][y] != 0 and board[x][y] < shark_size and board[x][y] != 9: # 상어 사이즈가 9가되면 
            fish.append((x,y,dist))
            min_dist = dist 
            continue
        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy


            # 범위를 벗어나면 패스
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            # 이미 방문했으면 패스
            if visited[nx][ny]:
                continue

            if board[nx][ny] > shark_size: # 물고기크기가 아기상어보다 크면 패스
                continue
            
            dq.append((nx, ny, dist+1))
            visited[nx][ny] = True
       
    if not fish:
        return -1, -1, -1
    
    fish.sort()
    x,y,dist = fish[0]
    board[r][c] = 0
    board[x][y] = 9

    return x, y, dist


res = 0
eat_cnt = 0
shark_size = 2

r, c = find_shark()

while True:
    r, c, cnt = bfs(r,c)
   
    if cnt == -1: # 더이상 먹을 수 있는 상어가 없으면
        print(res)
        break
    else:
        eat_cnt += 1
        res += cnt
        if shark_size == eat_cnt: # 먹은 횟수와 상어의 크기가 같아지면
            # print(f"상어크기커짐 {shark_size} -> {shark_size+1}")
            shark_size += 1       # 크기 1증가
            eat_cnt = 0           # 먹은 횟수는 초기화

