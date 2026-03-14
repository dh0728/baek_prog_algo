import sys
import heapq
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split())

is_see = list(map(int, input().split()))
nodes = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    nodes[a].append((b,c))
    nodes[b].append((a,c))

def dijkstra(start,end):
    dist = [INF] * N
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        curr_cost, curr = heapq.heappop(pq)

        if curr_cost > dist[curr]:
            continue

        if curr == end:
            return curr_cost
        

        for next, next_cost in nodes[curr]:

            if is_see[next] and next != end: # 적의 시야에 보이면 패스(도착지 제외)
                continue
            
            if curr_cost + next_cost < dist[next]:
                dist[next] = curr_cost + next_cost
                heapq.heappush(pq, (dist[next], next))

    return dist[end]

res =dijkstra(0, N-1)

if res == INF:
    print(-1)
else:
    print(res)