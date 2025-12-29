import sys
import heapq
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

arr = []

for _ in range(N):
    n, start, end = map(int, input().split())
    arr.append((n, start, end))

def solution():
    
    arr.sort(key= lambda x: x[1]) # 시작시간 -> 종료 시간 순으로 정렬

    h = []
    for n, start, end in arr:
        if h and h[0] <= start: # h[0]은 현재 강의중 가장 먼저 끝나는 강의
            heapq.heappop(h)
        heapq.heappush(h, end)

    print(len(h))



if __name__ == "__main__":
    solution()

