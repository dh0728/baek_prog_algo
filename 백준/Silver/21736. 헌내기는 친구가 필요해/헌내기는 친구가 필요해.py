import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    global cnt
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    q=deque()
    q.append([x,y])
    visited=[[0]*M for _ in range(N)]
    visited[x][y]=1

    while q:
        i,j =q.popleft()
        for dx, dy in dxy:
            nx= i+dx
            ny= j+dy
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if visited[nx][ny]:
                continue
            if campus[nx][ny]=='O': # 빈공간이면
                visited[nx][ny]=1
                q.append([nx,ny])
            elif campus[nx][ny]=='P': # 사람이면
                visited[nx][ny]=1
                cnt+=1
                q.append([nx,ny])
    return
N , M =map(int,input().split())
campus=[list(input().strip()) for _ in range(N)]
cnt=0

for i in range(N):
    for j in range(M):
        if campus[i][j]=='I':
            bfs(i,j)
if cnt ==0:
    print('TT')
else:
    print(cnt)