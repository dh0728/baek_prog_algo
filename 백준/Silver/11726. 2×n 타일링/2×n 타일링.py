import sys
input=sys.stdin.readline

N = int(input())
dp=[0]*1001
dp[1]=1
dp[2]=2
dp[3]=3

if N <= 3:
    print(dp[N]%10007)
else:
    if dp[N]:
        print(dp[N]%10007)
    else:
        for i in range(4,N+1): # 점화식은 dp[n]= dp[n-1] + dp[n-2]
            dp[i]=dp[i-1]+dp[i-2]
        print(dp[N]%10007)