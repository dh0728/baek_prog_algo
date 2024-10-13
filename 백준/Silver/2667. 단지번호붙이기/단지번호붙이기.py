import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

from collections import deque
def bfs(i,j):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    q=deque()
    q.append([i,j])

    cnt=1 # 단지에 있는 집수
    visited[i][j]=1

    while q:
        x,y = q.popleft()
        for dx,dy in dxy:
            nx= x+dx
            ny= y+dy
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if visited[nx][ny]:
                continue
            if maps[nx][ny]:
                visited[nx][ny]=1
                cnt+=1
                q.append([nx,ny])
    return cnt

N=int(input())
maps= [list(map(int,input().strip())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
result=[]
for i in range(N):
    for j in range(N):
        if visited[i][j]==0 and maps[i][j]: #방문한적 없고 집이 있으면
            n=bfs(i,j)
            result.append(n)

result.sort()
print(len(result))
for n in result:
    print(n)









