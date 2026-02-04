import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N, M, X = map(int, input().split())
nodes = [[] for _ in range(N+1)]  
node_reversed = [[] for _ in range(N+1)]  


for _ in range(M):
    s, e, t = map(int,input().split())
    nodes[s].append((e,t))
    node_reversed[e].append((s,t))


def counting_time(start, nodes):

    dq = deque([(start, 0)])
    dijk = [INF] * (N+1) 
    # dijk[start] = 0
    
    while dq:
        node, time = dq.popleft()

        if dijk[node] < time:
            continue

        for next_node, next_time in nodes[node]:
            if dijk[next_node] > time + next_time:
                dijk[next_node] = time + next_time
                dq.append((next_node, dijk[next_node]))

    return dijk



dijk = counting_time(X, nodes)
dijk_reversed = counting_time(X, node_reversed)
dijk[X] = 0
dijk_reversed[X] = 0

res = 0

for i in range(1,N+1):
    t = dijk[i] + dijk_reversed[i]
    if res < t:
        res = t

print(res)

