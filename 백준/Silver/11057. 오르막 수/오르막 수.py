import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

dp = [1] * 10

if N == 1:
    print(10)
else:
    for i in range(2, N+1):
        for j in range(1,10):
            dp[j] = dp[j] + dp[j-1]
    print( sum(dp)%10007)
 

