import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(s,e):
    global min_cnt
    dxy= [[0,1],[1,0],[0,-1],[-1,0]]
    # visited=[[0]*M for _ in range(N)]
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # 3차원으로 벽을 부순상태와 안부순 상태 구분

    q=deque()
    q.append([s,e,1,1]) # i, j, 칸수, 벽을 부술수 있는 횟수
    visited[s][e][1]=1

    while q:
        x, y ,cnt, block= q.popleft()
        if x==N-1 and y==M-1: # 목표지점 도착하면
            if cnt < min_cnt: # 최소경로 더작은걸로 바꾸기
                min_cnt =cnt
        for dx, dy in dxy:
            ni = x+dx
            nj = y+dy
            if ni<0 or ni>=N or nj <0 or nj >=M: #경로 벗어나기
                continue
            # 벽이 아닌 경우
            if maps[ni][nj]==0:
                if visited[ni][nj][block]==0:
                    visited[ni][nj][block]=1
                    q.append([ni,nj,cnt+1,block])
            # 벽을 만난 경우
            else:
                if block and visited[ni][nj][0]==0: # 부술 횟수 남아있으면
                    visited[ni][nj][0]=1
                    q.append([ni,nj,cnt+1,0])

    return


N , M = map(int,input().split())
maps= [list(map(int,input().strip())) for _ in range(N)]
min_cnt=N*M+1
bfs(0,0)
if min_cnt == N*M+1:
    print(-1)
else:
    print(min_cnt)