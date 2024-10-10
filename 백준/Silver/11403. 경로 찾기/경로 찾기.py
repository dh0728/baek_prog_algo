import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

from collections import deque
def bfs(i):
    q =deque()
    q.append(i)
    visited=[0]*N

    while q:
        x = q.popleft()

        for j in range(N):
            if visited[j]:
                continue
            if arr[x][j]==1:
                q.append(j)
                visited[j]=1
                result[i][j]=1


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

result=[[0]*N for _ in range(N)]
for i in range(N):
    bfs(i)

for row in result:
    print(' '.join(map(str, row)))