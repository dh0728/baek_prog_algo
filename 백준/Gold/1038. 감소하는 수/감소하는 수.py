import sys
from itertools import combinations
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

def solution():

    nums = []
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for r in range(1, 11):
        for comb in combinations(digits, r):
            # 조합은 오름차순으로 나옴
            val = 0
            for d in reversed(comb):
                val = val * 10 + d
            nums.append(val)
    
    nums.sort()

    if N >= len(nums):
        print(-1)
    else:
        print(nums[N])

if __name__ == "__main__":
    solution()


