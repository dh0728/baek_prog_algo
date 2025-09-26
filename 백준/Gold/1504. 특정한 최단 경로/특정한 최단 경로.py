import sys
import heapq
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 정점 개수, 간선 수
N ,E = map(int,input().split())

INF = 10**18

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# 꼭 거쳐가야하는 노드 두개
v1, v2 = map(int, input().split())

def dijkstra(start):

    dist = [INF] * (N + 1)
    dist[start] = 0

    pq = [(0,start)]

    while pq:
        d, x = heapq.heappop(pq)
        
        if d > dist[x]:
            continue

        for nx, w in graph[x]:
            nd = d + w

            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(pq, (nd, nx))
        
    return dist

def safe_sum(*vals):

    s = 0
    for v in vals:
        if v >= INF:
            return INF
        s += v
    return s

def solution():

    d1 = dijkstra(1)
    dV1 = dijkstra(v1)
    dV2 = dijkstra(v2)

    # 경로A = 1 → v1 → v2 → N
    pathA = safe_sum(d1[v1], dV1[v2], dV2[N])
    
    # 경로B = 1 → v2 → v1 → N
    pathB = safe_sum(d1[v2], dV2[v1], dV1[N])

    ans = min(pathA, pathB)

    if ans >= INF:
        print(-1)
    else:
        print(ans)

            

if __name__ == "__main__":
    solution()


