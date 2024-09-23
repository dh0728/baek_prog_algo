import sys
input=sys.stdin.readline


N = int(input())
dp=[0]*1001
dp[1]=1
dp[2]=3
dp[3]=5

# N >=4 부터 dp[N-1]에 2*1 직사각형 타일 하나를 붙이는 경우와
# dp[N-2]에 2*2 타일과 1*2 두개를 붙인 정사각형 타일을 붙인 경우의 합이다.
if N <= 3:
    print(dp[N]%10007)
else:
    if dp[N]:
        print(dp[N]%10007)
    else:
        for i in range(4,N+1): # 점화식은 dp[n]= dp[n-1] + 2*dp[n-2]
            dp[i]=dp[i-1]+2*dp[i-2]
        print(dp[N]%10007)