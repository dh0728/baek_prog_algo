import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

from collections import deque
def bfs(s):
    global cnt
    q=deque()
    q.append(s)
    visited[s]=1

    while q:
        node= q.popleft()
        for n in tree[node]:
            if visited[n]: #이미 방문한 노드면 pass
                continue
            visited[n]=1
            q.append(n)
    cnt+=1 # 탐색 다했으면 연결요소 개수 +1
    return

N,M = map(int,input().split())
tree=[[] for _ in range(N+1)]

for _ in range(M):
    p1,p2=map(int,input().split())
    tree[p1].append(p2) # 무방향 그래프
    tree[p2].append(p1)

cnt =0
visited =[0]*(N+1)
for i in range(1,N+1):
    if not visited[i]: # 아직 방문 않나 노드가 있다면
        bfs(i)         # 너비 우선 탐색으로 탐색
print(cnt)