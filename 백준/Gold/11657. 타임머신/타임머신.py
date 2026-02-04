import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split()) # N : 도시의 수 M: 버스 노선의 수
dist = [INF] * (N +1)
graph= []


def bellman_ford(start):

    # 시작 노드는 0으로 초기화
    dist[start] = 0

    # N 번 반복
    # N - 1번 탐색하고 마지막 한번은 Negative cycle 존재 확인
    for i in range(N):
        # 매 반복마다 모든 간선을 확인하며 갱신
        for j in range(M):
            curr_node, next_node, time = graph[j]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[curr_node] != INF and dist[curr_node] + time < dist[next_node]:
                dist[next_node] = dist[curr_node] + time

                # N번째 반복에서 갱신되는 값이 있으면 Negative cycle 존재
                if i == N-1:
                    return False

    return True
    
# C == 0 인 경우 - 순간 이동
# C < 0 인 경우 - 타임 머신
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A,B,C))

if bellman_ford(1):
    for i in range(2, N+1):
        if dist[i] != INF:
            print(dist[i])
        else:
            print(-1)
else:
    print(-1)
