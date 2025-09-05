import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def bfs(N, nodes):

    visited = [False] * (N + 1)
    queue = deque()
    cnt = 0

    for i in range(1,N+1):
        
        if visited[i]:
            continue
        cnt += 1
        visited[i] = True
        queue.append(i)

        while queue:
            curr_node = queue.popleft()

            for n in nodes[curr_node]:
                if visited[n]:
                    continue

                queue.append(n)
                visited[n] = True
                
    return cnt


def solution():

    t = int(input())

    for _ in range(t):

        N = int(input())

        arr = list(map(int, input().split()))

        nodes = [[] for _ in range(N + 1)] 

        for i in range(N): # 양방향이므로
            nodes[i+1].append(arr[i])
            nodes[arr[i]].append(i+1)

        answer = bfs(N, nodes)
        print(answer)

if __name__ == "__main__":
    solution()


