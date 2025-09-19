import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# N : 수빈이 위치
# K : 동생 위치
N, K = map(int,input().split())

SIZE = 100000

def bfs():

    visited = [SIZE] * (SIZE  + 1)

    q = deque()

    q.append(N)
    visited[N] = 0

    while q:
        x = q.popleft()

        if x == K:
            return visited[x]
        
        t = visited[x]
        nx = x * 2

        if 0 <= nx <= SIZE and visited[nx] > t:
            q.appendleft(nx)
            visited[nx] = t

        for n in [1,-1]:
            nx = n + x

            if nx < 0 or nx > SIZE or visited[nx] <= t  + 1:
                continue
            q.append(nx)
            visited[nx] = t + 1

    return visited[K]

def solution():

    print(bfs())

            
if __name__ == "__main__":
    solution()


