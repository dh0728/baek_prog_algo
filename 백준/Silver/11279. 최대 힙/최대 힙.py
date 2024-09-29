import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

import heapq

N= int(input())
heap=[]

for _ in range(N):
    n = int(input())
    if n==0:
        if heap:
            print(-heapq.heappop(heap)) # 다시 - 붙여서 원상복구
            continue
        print(0)
    else:
        heapq.heappush(heap,-n) # heapq 모듈을 쓸 경우 최대힙은 -을 넣어서 넣기