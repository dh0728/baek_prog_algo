import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

wines = [int(input().strip()) for _ in range(N)]

def solution():
    dp = [0] * N
    dp[0] = wines[0] 

    if N > 1:
        dp[1] = wines[0] + wines[1] 
    
    if N > 2:
        dp[2] = max(dp[1], wines[1] + wines[2], wines[0] + wines[2])

    for i in range(3, N):
        # 현재 포도주와 이전 포도주를 마시는 경우 (전전 포도주 마시지 X)
        # 현재 포도주와 전전 포도주를 마시는 경우 (이전 포도주 마시지 X)
        # 이전 포두주와 전전 포도주를 마시는 경우 (현재 포도주 마시지 X)
        dp[i] = max(wines[i] + wines[i - 1] + dp[i - 3], wines[i] + dp[i - 2], dp[i - 1])

    print(dp[-1])

if __name__ == "__main__":
    solution()

