import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
nums = []

def solution():
    for _ in range(N):
        a, b = map(int, input().split())
        nums.append(b - a)

    nums.sort()

    res = 0

    if N % 2 == 0: # 마법사 수가 짝수이면
        s = N // 2 - 1
        res = nums[s + 1] - nums[s] + 1
    else:
        res = 1

    print(res)


    return

if __name__ == "__main__":
    solution()


