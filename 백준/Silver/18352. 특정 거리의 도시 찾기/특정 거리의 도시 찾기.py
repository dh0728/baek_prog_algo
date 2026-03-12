import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N, M, K, X = map(int,input().split())
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)


def dijkstra(start):
    dist = [INF] * (N+1)
    dq = deque([(start,0)])
    dist[start] = 0

    while dq:
        curr, curr_cost = dq.popleft()

        if curr_cost > dist[curr]:
            continue

        for next in nodes[curr]:
            if curr_cost + 1 < dist[next]:
                dist[next] = curr_cost + 1
                dq.append((next, dist[next]))

    return dist 

dist = dijkstra(X)

if K in dist:
    for i, k in enumerate(dist):
        if k == K:
            print(i)
else:
    print(-1)