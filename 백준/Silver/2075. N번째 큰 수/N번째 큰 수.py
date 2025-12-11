import sys
import heapq
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())


def solution():

    heap = []

    for _ in range(N):
        nums = list(map(int, input().split()))

        for num in nums:
            if len(heap) < N: # 힙크기가 N 보다 작으면
                heapq.heappush(heap, num) # 힙에 삽입
            else:
                if heap[0] < num: 
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

    print(heap[0])
  

if __name__ == "__main__":
    solution()


