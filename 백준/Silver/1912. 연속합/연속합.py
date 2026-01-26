import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

arr = list(map(int, input().split()))

def solution():

    dp = [-100000] * N
    dp[0] = arr[0]

    for i in range(1, N):
        dp[i] = max(dp[i -1] + arr[i], arr[i])

    print(max(dp))

    return


if __name__ == "__main__":
    solution()

