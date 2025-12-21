import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
SIZE = 100000

dir= [2, 1, -1]

def bfs(start, end):
    v = [SIZE] * (SIZE + 1) # 방문 기록
    q = deque([(start, 0)]) # 출발지, 시간
    min_time = SIZE
    cnt = 0
    while q:
        curr, time = q.popleft()

        if curr == end: # 동생 찾았는데
            if time < min_time: # 가장 빠른 시간이면
                min_time = time # 가장 빠른 시간 갱신
                cnt = 1         # 찾는 방법 수 초기화
            elif time == min_time: # 현재 가장 빠른 시간과 같으면
                cnt += 1
            else:
                continue # 크면 패스

        for d in dir:
            if d == 2:
                next = curr * 2
            else:
                next = curr + d
            
            if  next < 0 or next > SIZE:
                continue

            if time + 1 <= v[next]:
                if time + 1 < v[next]:
                    v[next] = time + 1
                q.append((next, time+1))
    
    return min_time, cnt
        

def solution():
    min_time, cnt = bfs(N,K)
    print(min_time)
    print(cnt)

if __name__ == "__main__":
    solution()


