import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N , M = map(int, input().split())
graph = [[] for _ in range(N+1)] # (연결된 노드, 길이) 이런식으로 저장됨

def bfs(n1, n2):

    q = deque()
    q.append((n1, 0))
    visited = [0] * (N + 1)
    visited[n1] = 1 # 출발노드 방문처리

    while q:
        n, l = q.popleft()

        if n == n2: # 목적지에 도착했으면
            return l
        
        for next, d in graph[n]:
            if not visited[next]:
                visited[next] = True
                q.append((next, l+d))

    return -1

def solution():

    for _ in range(N-1):
        node1, node2, lens = map(int, input().split()) # 노드1, 노드2, 길이
        graph[node1].append((node2, lens)) 
        graph[node2].append((node1, lens))

    for _ in range(M):
        node1, node2 = map(int,input().split())
        print(bfs(node1,node2)) 


if __name__ == "__main__":
    solution()


