import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input().strip()) for _ in range(N)]

def solution():

    dp = [0] * (K+1)
    dp[0] = 1
    for c in coins:
        for j in range(c, K + 1):
            dp[j] = dp[j] + dp[j - c] # 점화식 dp[n] = dp[n] + dp[n- 현재 사용한 동전의 크기]

    print(dp[K])

if __name__ == "__main__":
    solution()

