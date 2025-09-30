import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 정점 개수
N = int(input())

graphs = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, w = map(int,input().split())
    graphs[u].append((v, w))
    graphs[v].append((u, w))

def farthest(s):
    
    visited = [False] * (N + 1)
    visited[s] = True
    stack = [(s, 0)]
    max_dist = 0
    max_node = s

    while stack:

        x, d = stack.pop()
        if d > max_dist:
            max_dist = d
            max_node = x

        for  nx , w in graphs[x]:
            if not visited[nx]:
                visited[nx] = True
                stack.append((nx, d + w))

    return max_node, max_dist

def solution():

    if N == 1:
        print(0)
    else:
        a, _  = farthest(1)
        _, d = farthest(a)
        print(d)
    return

if __name__ == "__main__":
    solution()