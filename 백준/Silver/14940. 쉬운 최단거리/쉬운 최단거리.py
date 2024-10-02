import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    q=deque()
    q.append([x,y,0])
    visited[x][y]=0
    while q:
        i, j, cnt = q.popleft()
        for dx ,dy in dxy:
            ni = i +dx
            nj = j +dy
            if ni <0 or ni>=n or nj<0 or nj>=m: #범위 벗어나면 패스
                continue
            if visited[ni][nj] !=-1: #이미 방문했으면 패스
                continue
            if arr[ni][nj]==0: # 갈 수 없는 길이면
                visited[ni][nj]=0
                continue
            visited[ni][nj]=cnt+1
            q.append([ni,nj,cnt+1])


n , m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
visited= [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            bfs(i,j)
            
for i in range(n):
    for j in range(m):
        if arr[i][j]==0 and visited[i][j]==-1: # 도달할 수 없는 위치에 있는 장애물 0으로 만들기
            visited[i][j]=0

for i in range(n):
    print(*visited[i])