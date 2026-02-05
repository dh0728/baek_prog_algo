import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N = int(input().strip())
M = int(input().strip())

graph = [[] for _ in range(N+1)]
dist = [INF for _ in range(N+1)]
visited = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijksra(start, end):

    dq = deque([(start,0,[start])])
    dist[start] = 0
    res = []

    while dq:
        curr_node, curr_cost, curr_visited = dq.popleft()
        # 이미 이전에 더 적은 가중치로 갱신한 적이 있다면
        if dist[curr_node] < curr_cost:
            continue

        for next_node, cost in graph[curr_node]:
            # print(f'현재 노드 : {curr_node} 다음 노드 :{next_node} ')
            
            # 최단 거리가 갱신되면
            if dist[next_node] > curr_cost + cost:
                dist[next_node] = curr_cost + cost
                visited[next_node] = curr_visited + [next_node]
                dq.append((next_node, dist[next_node], visited[next_node]))

    return res

s, e = map(int, input().split())
dijksra(s, e)
print(dist[e])
print(len(visited[e]))
for n in visited[e]:
    print(n, end=" ")

