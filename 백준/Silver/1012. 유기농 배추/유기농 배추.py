from collections import deque
def bfs(x,y):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    visited[x][y]=1
    q=deque()
    q.append([x,y])
    while q:
        i,j=q.popleft()
        for dx, dy in dxy:
            ni=i+dx
            nj=j+dy
            if 0>ni or ni>=N or 0>nj or nj>=M: #범위 벗어나면 패스
                continue
            if visited[ni][nj]==1: #이미 방문했으면 패스
                continue
            if arr[ni][nj]==0: # 배추가 없는 곳이면 패스
                continue
            visited[ni][nj]=1 # 다음 배추에 방문처리
            q.append([ni,nj]) # 큐에 넣기
    return

T=int(input())
for tc in range(1,T+1):
    # M 배추밭 가로길이, N 세로길이, K 배추가 심어져 있는 위치의 개수
    M, N, K=map(int,input().split())
    arr=[[0]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        arr[y][x]=1

    cnt=0
    visited=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] ==1 and visited[i][j]==0:
                bfs(i,j)
                cnt+=1 # 새로운 배추구역을 찾을 때마다 cnt +1

    print(cnt)