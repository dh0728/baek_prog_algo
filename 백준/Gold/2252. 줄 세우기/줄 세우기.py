import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상정렬 함수
def topology_sort():
    res = []
    dq =deque()

    for i in range(1,N+1):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        
        curr = dq.popleft()
        res.append(curr)

        for next in graph[curr]:
            indegree[next] -= 1

            # 진입차수가 0이면 큐에 넣기
            if indegree[next] == 0:
                dq.append(next)
    return res

res = topology_sort()

print(*res)