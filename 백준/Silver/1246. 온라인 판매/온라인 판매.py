import sys
from collections import defaultdict
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split()) # N = 달걀의 수, M = 잠재적인 고객 수


def solution():
    # 각자 밝힌 가격을 살수 있는 가격
    arr = [int(input().strip()) for _ in range(M)]
    arr.sort(reverse = True)

    if N < M:
        customs = arr[:N]
    else:
        customs = arr.copy()
    
    res = 0
    p =0
    for i in range(len(customs) - 1, -1, -1):
        temp = customs[i] * (i+1)
        if temp > res:
            res = temp
            p = customs[i]
    
    print(p, res)
        
if __name__ == "__main__":
    solution()

