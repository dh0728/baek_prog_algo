import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

V, E = map(int,input().split()) # V : 마을 갯수 E : 도로의 갯수

graph = [[INF] * (V + 1) for _ in range(V+1)]


for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c


for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = INF

for i in range(1, V+1):
    ans = min(ans, graph[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)

