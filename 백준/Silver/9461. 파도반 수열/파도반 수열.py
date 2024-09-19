import sys
input=sys.stdin.readline

def find_P():
    if dp[N]: 
        return dp[N]
    for i in range(6,N+1):
        dp[i]=dp[i-1]+dp[i-5] # N>=6 일때 변의 길이는 N-1번째 변의 길이 + N-5번째 변의 길이의 합
    return dp[N]

T=int(input())
dp=[0]*101
dp[1],dp[2],dp[3]=1,1,1
dp[4]=2
dp[5]=2
for tc in range(1, T+1):
    N=int(input())
    print(find_P())