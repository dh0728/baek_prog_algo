import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

from collections import deque
def bfs(store,x,y):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    visited= [[0]*(N+1) for _ in range(M+1)]
    q=deque()
    q.append([x,y,0])
    visited[x][y]=[-1] # 시작 지점 방문표시

    while q:
        i,j, cnt= q.popleft()
        if maps[i][j]==store:
            return cnt
        for dx,dy in dxy:
            nx= i+dx
            ny= j+dy
            if nx<0 or nx >M or ny<0 or ny>N: #범위 벗어나면 패스
                continue
            if visited[nx][ny]==-1: # 이미 방문했으면
                continue
            if nx == 0 or nx==M or ny == 0 or ny == N: # 경계선에만 있어야함
                visited[nx][ny]=-1
                q.append([nx,ny,cnt+1])



N, M = map(int,input().split()) # 블록의 가로 세로 길이
S = int(input()) # 상점의 개수

# 상점의 방향(1:북,2:남,3:서,4:동), 왼쪽 경계로 부터 거리
maps = [[0]*(N+1) for _ in range(M+1)] # 맵 초기화
for i in range(1,S+1): # 맵에 상점들 초기화
    direction, distance = map(int,input().split())
    if direction ==1: #북
        maps[0][distance]=i
    elif direction ==2: # 남
        maps[M][distance]=i
    elif direction ==3: # 서
        maps[distance][0]=i
    elif direction ==4: # 동
        maps[distance][N]=i

direction, distance = map(int,input().split())
x,y=0,0
if direction ==1: #북
    x,y= 0,distance
elif direction ==2: # 남
    x,y=M,distance
elif direction ==3: # 서
    x,y=distance,0
elif direction ==4: # 동
    x,y=distance,N

result=0
for i in range(1,S+1):
    n=bfs(i,x,y)
    result +=n

print(result)