import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
l = [int(input().rstrip()) for i in range(n)]
pq = [-l[i] for i in range(1,n)]
heapq.heapify(pq)
res = 0
while pq and l[0]<=-pq[0]:
    l[0]+=1
    t = heapq.heappop(pq)
    heapq.heappush(pq,t+1)
    res+=1
print(res)