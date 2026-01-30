import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX_SIZE = 10001

N, M = map(int, input().split())

arr = list(map(int, input().split()))

def solution():

    left = 0
    sum_num = 0
    res = 0

    for right in range(N):
        sum_num += arr[right]
        
        while sum_num > M:
            sum_num -= arr[left]
            left +=1

        if sum_num == M:
            res +=1
            sum_num -= arr[left]
            left += 1

    print(res)


if __name__ == "__main__":
    solution()

