import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline
import heapq

N= int(input())
h=[]
# x != 0 이면 배열에 x 추가 x == 0 이면 배열에서 절댓값이 가장 작은 값을 출력
# 비어있는데 출력하라고 하면 0 출력
for _ in range(N):
    x=int(input())
    if x ==0: # 0이면
        if h: # 힙에 값 있으면
            pop_x=heapq.heappop(h)
            print(pop_x[1]) # 절댓값 작은 수의 원래값 추출
        else:
            print(0) # 비어있으면 0출력
    else: # 0 아니면
        heapq.heappush(h,(abs(x),x)) #절댓값, 원래값 넣기