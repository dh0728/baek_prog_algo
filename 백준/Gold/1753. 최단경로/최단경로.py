import sys
import heapq
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 정점 개수, 간선 수
V ,E = map(int,input().split())

# 시작 정점의 번호
K = int(input())

INF = 10**18

graphs = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    graphs[u].append((v, w))

def dikstra(s):

    dist = [INF] * (V + 1)
    dist[s] = 0
    pq = [(0,s)]

    while pq:

        d, x = heapq.heappop(pq)

        if d > dist[x]:
            continue

        for nx, w in graphs[x]:
            nw = d + w

            if nw < dist[nx]:
                dist[nx] = nw
                heapq.heappush(pq, (nw, nx))

    return dist


def solution():

    dist = dikstra(K)

    for i in range(1, V+1):
        if dist[i] >= INF:
            print("INF")
        else:
            print(dist[i])

if __name__ == "__main__":
    solution()


