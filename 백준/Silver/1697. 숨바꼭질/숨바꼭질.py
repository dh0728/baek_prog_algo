import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [0] * 100001  # 방문 여부를 저장하는 리스트 (0 ~ 100000)
    q = deque()
    q.append((N, 0))  # (현재 위치, 걸린 시간)
    visited[N] = 1  # 시작 위치는 방문 처리

    while q:
        X, cnt = q.popleft()

        if X == K:  # 수빈이가 동생 위치에 도착하면 시간 반환
            return cnt

        # 이동할 수 있는 세 가지 경우를 처리
        for next in [X * 2, X + 1, X - 1]:
            if 0 <= next <= 100000 and not visited[next]:  # 범위 체크와 방문 여부 체크
                visited[next] = 1
                q.append((next, cnt + 1))

# 입력 받기
N, K = map(int, input().strip().split())

# BFS 실행 후 결과 출력
result = bfs()
print(result)