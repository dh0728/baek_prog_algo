import sys
from itertools import combinations
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip()) 

# 줄어드는 수가 생길 수 있는 숫자 범위 : 0 ~ 9876543210 
def solution():
    
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []

    for i in range(1, 11):
        for numbers in combinations(nums, i):
            val = 0
            for n in reversed(numbers):
                val = val*10 + n 

            res.append(val) 

    res.sort()

    if N > len(res):
        print(-1)
    else:
        print(res[N -1])



if __name__ == "__main__":
    solution()
