import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
dp = [[0,0] for _ in range(N + 1)] # dp[자릿수][앞의 숫자 - 0 or 1] = 경우의 수

def solution():
    
    dp[1][1] = 1 # 1
     
    for i in range(2, N+1):
        dp[i][0] = dp[i-1][1] + dp[i-1][0]
        dp[i][1] = dp[i-1][0] 

    print(sum(dp[N]))
    return
    
if __name__ == "__main__":
    solution()

