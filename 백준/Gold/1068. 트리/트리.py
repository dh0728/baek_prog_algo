import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
nodes = list(input().split())
del_node = int(input())

tree = [[] for _ in range(N)]
root = 0

# 애초에 트리에 넣을때부터 삭제
for n in range(N):
    if nodes[n] == "-1":
        root = n
        continue
    
    if n == del_node: # 제거해야 하는 노드면 패스
        continue

    node = int(nodes[n])
    tree[node].append(n) # 트리에 자식노드 넣기

def dfs(root):

    q = deque()
    q.append(root)
    cnt = 0

    while q:
        n = q.popleft()

        if n == del_node: # 만약 제거한 노드이면
            continue

        if tree[n]: # 자식노드가 존재하면
            for node in tree[n]:
                q.append(node)
        else:
            cnt +=1
    
    return cnt

def solution():

    res = dfs(root)
    print(res)

if __name__ == "__main__":
    solution()


