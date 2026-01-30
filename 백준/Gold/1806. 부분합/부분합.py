import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX_SIZE = 100001

N, S = map(int, input().split())

arr = list(map(int, input().split()))

def solution():

    res = MAX_SIZE

    left = 0
    sum_num = 0
    
    for right in range(N):
        sum_num += arr[right]

        while sum_num >= S:
            res = min(res, right - left + 1)
            sum_num -= arr[left]
            left += 1

    if res == MAX_SIZE:
        print(0)
    else:
        print(res)

if __name__ == "__main__":
    solution()

