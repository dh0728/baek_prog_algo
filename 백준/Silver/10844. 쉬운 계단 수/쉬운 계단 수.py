import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MOD = 1000000000

N = int(input().strip())

def solution():
    
    if N == 1:
        print(9)
        return
    elif N == 2:
        print(17)
        return

    dp = [[0] * 10 for _ in range(N+1)] # dp[자릿수][앞의 숫자] = 경우의 수

    for i in range(1,10):
        dp[1][i] = 1

    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:    
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


    print(sum(dp[N]) % MOD)

if __name__ == "__main__":
    solution()

