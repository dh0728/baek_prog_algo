import sys
import heapq
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 10 ** 15

n, m, r = map(int, input().split()) # n : 지역의 개수, m : 수색 범위, r : 길의 개수
items = [0] + list(map(int, input().split())) # 지역별 아이템 개수
nodes = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    nodes[a].append([b,l])
    nodes[b].append([a,l])


def dijkstra(start):
    
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0,start)] # 거리, 노드

    while pq:
        d, curr = heapq.heappop(pq) 
        if d != dist[curr]:
            continue
        for next, w in nodes[curr]:
            nd = d + w
            if nd < dist[next]:
                dist[next] = nd
                heapq.heappush(pq, (nd, next))

    cnt = 0
    for i in range(1, n+1):
        if dist[i] <= m:
            cnt += items[i]

    return cnt

def solution():
    res = 0
    for i in range(1,n+1):
        num = dijkstra(i)
        if res < num:
            res = num

    print(res)


if __name__ == "__main__":
    solution()

