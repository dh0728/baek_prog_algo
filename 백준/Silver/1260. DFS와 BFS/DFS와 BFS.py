from collections import deque
def dfs(node):
    sort_node=[]
    visited = [0] * (N + 1)
    stack = []  # 스택 생성
    visited[node] = 1  # 시작정점 방문표시
    sort_node.append(node)
    curr_node = node  # 현재정점
    while True:
        for n in graph[curr_node]:
            if visited[n]==1:
                continue
            stack.append(curr_node)
            curr_node=n
            sort_node.append(curr_node)
            visited[curr_node]=1
            break
        else:
            if stack:
                curr_node = stack.pop()
            else:  # 되돌아갈 곳 없으면 그대로 종료
                break  # while문 break
    return sort_node

def bfs(start):
    sort_node=[]
    v=[0]*(N+1)
    q=deque()
    q.append(start)
    v[start]=1 # 시작노드 방문표시
    while q:
        node=q.popleft()
        sort_node.append(node)
        for n in graph[node]:
            if v[n]: # 방문한 적이 있다면 패스
                continue
            v[n]=1
            q.append(n)
    return sort_node

N, M, V=map(int,input().split()) # N 정점의 개수, M 간선의 개수, V 탐색시작 정점의 번호

arr=[list(map(int,input().split())) for _ in range(M)]
graph=[[] for _ in range(N+1)]

for a in arr: # 연결리스트 만들기(양방향)
    graph[a[0]].append(a[1])
    graph[a[1]].append(a[0])

for g in graph: # 정렬을 하고 올바르게 탐색됨
    g.sort()

dfs_sort=dfs(V) # 정점의 개수(종료조건), 시작노드 깊이우선탐색으로 탐색
bfs_sort=bfs(V) # 너비우선탐색으로 탐색
print(*dfs_sort)
print(*bfs_sort)