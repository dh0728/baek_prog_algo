import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def solution():

    N = int(input())

    tree = [[] for _ in range(N+1)]
    
    for _ in range(N -1):
        n1, n2 = map(int, input().split())
        tree[n1].append(n2)
        tree[n2].append(n1)

    # 1.깊이와 1칸 부모 계산 (BFS/DFS)
    LOG = (N).bit_length() # 2*LOG > N
    
    parent = [[0] * (N + 1) for _ in range(LOG)] # 노드의 2^k 번째 조상을 저장하는 테이블
                                                 # Parent[x][k] = Parent[Parent[x][k - 1]][k - 1] 이걸 이해해야함
    depth = [0] * (N + 1) # 각 노드가 루트로부터 몇 칸 아래에 있는지 기록

    q = deque([1])
    visited = [False] * (N + 1)
    visited[1] = True

    while q:
        u = q.popleft()
        for v in tree[u]:
            if not visited[v]:
                visited[v] = True
                parent[0][v] = u
                depth[v] = depth[u] + 1
                q.append(v)

    
    # 2 이진 리프팅 테이블 채우기 
    for k in range(1, LOG):
        up = parent[k - 1]
        cur = parent[k]
        for v in range(1, N + 1):
            cur[v] = up[up[v]]

    # 2. 이진 리프팅 테이블 채우기
    def LCA(a,b):
        if depth[a] < depth[b]:
            a, b = b, a
        # a를 b의 깊이까지 끌어올리기
        diff = depth[a] - depth[b]
        bit = 0
        while diff:
            if diff & 1:
                a = parent[bit][a]
            diff >>= 1
            bit += 1
        if a == b:
            return a
        # 동시에 위로 점프(큰 k부터)
        for k in range(LOG - 1, -1, -1):
            if parent[k][a] != parent[k][b]:
                a = parent[k][a]
                b = parent[k][b]
        return parent[0][a]

    

    M = int(input())

    out = []

    for _ in range(M):
        u, v = map(int, input().split())
        out.append(str(LCA(u,v)))

    print("\n".join(out))



if __name__ == "__main__":
    solution()


