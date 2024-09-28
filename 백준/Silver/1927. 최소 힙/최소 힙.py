import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

import heapq

N=int(input())
heap =[]
for _ in range(N):
    n=int(input())
    if n==0: # 0이면 가장 작은 값 출력후 제거
        if len(heap)==0: # 비어있으면 0출력
            print(0)
            continue
        result= heapq.heappop((heap))
        print(result)
    else: # 아니면 삽입
        heapq.heappush(heap,n)

