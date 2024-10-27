import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

from collections import deque
def bfs(start):
    visited=[-1]*(N+1)
    q=deque()
    q.append(start) # 핸재노도 전에 노드
    visited[start]=0

    while q:
        current_node= q.popleft()
        for node in tree[current_node]:
            if visited[node] != -1: #이미 방문한 노드이면 패스
                continue
            visited[node]=current_node
            q.append(node)
    return visited

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    node1, node2 = map(int,input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

result=bfs(1)
for i in range(2,N+1):
    print(result[i])