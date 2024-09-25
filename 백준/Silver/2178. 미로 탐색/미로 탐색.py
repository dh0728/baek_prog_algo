import sys
input=sys.stdin.readline
from collections import deque

def bfs(i,j):
    visited=[[0]*M for _ in range(N)]
    q=deque()
    q.append([i,j,1]) # i,j,이동 칸수
    while q:
        x, y, cnt = q.popleft()
        if x==N-1 and y==M-1:
            return cnt
        for dx, dy in dxy:
            ni=x+dx
            nj=y+dy
            if ni <0 or ni >=N or nj<0 or nj>=M:
                continue
            if visited[ni][nj]:
                continue
            if arr[ni][nj]:
                visited[ni][nj]=1
                q.append([ni,nj,cnt+1])
    return 0

N, M = map(int,input().split())
arr=[list(map(int,input().strip())) for _ in range(N)]

dxy=[[0,1],[1,0],[0,-1],[-1,0]]
result=bfs(0,0)
print(result)