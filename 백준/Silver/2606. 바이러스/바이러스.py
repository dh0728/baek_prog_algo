from collections import deque
def bfs(node):
    global cnt
    visited = [0] * (N + 1)
    q=deque()
    q.append(node)
    visited[node]=1
    while q:
        n = q.popleft()
        for next_n in graph[n]:
            if visited[next_n]:
                continue
            cnt+=1
            visited[next_n]=1
            q.append(next_n)
    return

N=int(input()) # 노드수
M=int(input()) # 간선수
arr=[list(map(int,input().split())) for _ in range(M)] # 간선 정보

graph=[[] for _ in range(N+1)]
for a in arr:
    graph[a[0]].append(a[1])
    graph[a[1]].append(a[0])

visited=[0]*(N+1)
cnt=0
bfs(1)
print(cnt)