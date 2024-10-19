import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

from collections import deque
def bfs(i):
    visited=[-1]*(N+1)

    q=deque()
    q.append(i)
    visited[i]=0

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] != -1: # 이미 방문했으면
                continue
            visited[next_node] = visited[node]+1
            q.append(next_node)

    return sum(visited[1:]) # i 노드가 주변 노드를 방문하는데 걸리는 케빈 베이컨 수는 visited를 다 더 한것


N , M = map(int,input().split()) # N 유저의 수 , M 관계의 수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

result = -1
min_cnt = 10**9
for i in range(1,N+1):
    cnt =bfs(i)
    if cnt < min_cnt:
        min_cnt =cnt
        result =i

print(result)