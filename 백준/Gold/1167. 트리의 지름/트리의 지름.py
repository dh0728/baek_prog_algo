import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

V = int(input().strip())

tree = [[] for _ in range(V+1)]

for _ in range(V):
    line = list(map(int,input().split()))
    n= line[0]
    i = 1
    while True:

        s = line[i]

        if s == -1:
            break
        i += 1
        d = line[i]
        tree[n].append((s,d))
        i += 1
        
def dfs(s):
    visited = [False for _ in range(V+1)]
    stack = []
    stack.append((s,0))
    visited[s] = True
    max_dist = (s,0)

    while stack:
        node, dist = stack.pop()

        # 최대 길이 갱신
        if dist > max_dist[1]:
            max_dist = (node,dist)
        
        for next in tree[node]:
            next_node = next[0]
            next_dist = next[1]

            if visited[next_node]:
                continue
            
            stack.append((next_node, dist + next_dist))
            visited[next_node] = True
    return max_dist

temp = dfs(1)
res = dfs(temp[0])

print(res[1])