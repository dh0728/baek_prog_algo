from collections import deque
import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def bfs():
    # 오, 아래, 왼, 오
    dxy=[[1,0],[0,1],[-1,0],[0,-1]]
    visited = [[0] * M for _ in range(N)]

    q=deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:  # 익어있는 상태의 토마토면 큐에 넣기
                q.append([i, j, 0])  # 현재 토마토 좌표, 날짜
                visited[i][j] = 1
    max_days=0
    while q:
        i,j,days=q.popleft()
        max_days=days
        for dx,dy in dxy:
            ni= i+dx
            nj= j+dy
            if ni<0 or ni>=N or nj<0 or nj>=M:
                continue
            if visited[ni][nj]: # 이미 방문했다면
                continue
            if tomato[ni][nj]==-1: #토마토가 없는 칸이면 패스
                continue
            if tomato[ni][nj]==0: # 인접한 곳에 안익은 토마토 발견하면
                visited[ni][nj]=1
                tomato[ni][nj] = 1
                q.append([ni,nj,days+1])
    return max_days

def exam_tomato(): # 안익은 토마토가 있는지 검사
    global result
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0: #안익은 토마토 있으면
                result =-1  # -1 삽입
                return


# M : 상자 가로칸, N: 세로, H: 높이
M,N=map(int,input().split())

# 1 = 익은 토마토 , 0 = 익지 않은 토마토 , -1 토마토 X
tomato=[list(map(int,input().split())) for _ in range(N)]

result=bfs()
exam_tomato()
print(result)