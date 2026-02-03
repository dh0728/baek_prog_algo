import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, K = map(int, input().split()) 

arr = [0] * (N+1)
tree = [0] * (N+1)

# i 번쨰 수까지 누적 합을 계산
def prefix_sum(i):
    res = 0
    while i > 0:
        res += tree[i]

        # 0이 아닌 마지막 비트만큼 빼면서 이동
        i -= (i & -i)
    return res

# i번째 수를 dif만큼 더하는 함수
def update(i, dif):
    while i <= N:
        tree[i] += dif
        i += (i & -i)

# start ~ end 까지의 구간 합
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)


for i in range(1,N+1):
    n = int(input().strip())
    arr[i] = n
    update(i, n)

def solution():

    for _ in range(M+K):
        a, b, c = map(int ,input().split())
        if a == 1:
            update(b,c - arr[b])
            arr[b] = c 
        else:
            print(interval_sum(b,c))

if __name__ == "__main__":
    solution()