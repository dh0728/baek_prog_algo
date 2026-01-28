import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
dp = [0] * (N+1) 

def solution():
    
    dp[1] = 1

    for i in range(2,N+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[-1])

    
if __name__ == "__main__":
    solution()

