import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N, M = map(int,input().split())

nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int ,input().split())
    nodes[a].append((b,c))
    nodes[b].append((a,c))

def dijkstra(start, end):
    dijk = [INF] * (N+1)
    dijk[start] = 0

    dq = deque([(start,0)])


    while dq:
        curr, curr_cost = dq.popleft()

        # 이미 더 짧은 거리로 처리된 적 있으면 스킵
        if dijk[curr] < curr_cost:
            continue

        if curr == end:
            continue

        for next, next_cost in nodes[curr]:

            if dijk[next] > next_cost + curr_cost:
                dijk[next] = next_cost + curr_cost
                dq.append((next, dijk[next]))

    return dijk[end]

res = dijkstra(1, N)
print(res)