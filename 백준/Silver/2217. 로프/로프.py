import sys
from collections import defaultdict
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
arr = []
def solution():
    
    for _ in range(N):
        arr.append(int(input().strip()))

    arr.sort(reverse=True)
    
    res = 0
    # 내림차순으로 정렬후 하나씩 로프를 추가
    for i in range(N):
        temp = arr[i] * (i + 1)
        if temp > res:
            res = temp

    print(res)

if __name__ == "__main__":
    solution()

