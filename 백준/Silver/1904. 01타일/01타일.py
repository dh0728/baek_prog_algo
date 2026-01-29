import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
dp = [0] * (N+1)

def solution():
    
    if N==1:
        print(1)
        return
    elif N==2:
        print(2)
        return

    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    print(dp[N])

if __name__ == "__main__":
    solution()

