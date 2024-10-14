import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

from collections import deque


def bfs():
    q=deque()
    visited = [0] * N
    q.append([0,0]) # idx, cnt
    visited[0]=1

    while q:
        idx, cnt =q.popleft() # 점프력

        for j in range(arr[idx],0,-1): # 점프해서 갈 수 있는 칸
            if idx+j >= N - 1:  # 오른쪽 끝에 도달 하면
                return cnt+1  # 점프 횟수 리턴
            if visited[idx+j]:
                continue
            visited[idx+j]=1
            q.append([idx+j,cnt+1])   # 짧은 순부터 차례로 넣기
    return -1

N= int(input())
arr=list(map(int,input().split()))

if N==1:
    print(0)
else:
    result=bfs()
    print(result)