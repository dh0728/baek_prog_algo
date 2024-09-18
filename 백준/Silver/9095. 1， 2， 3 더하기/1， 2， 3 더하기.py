import sys
input=sys.stdin.readline

T=int(input())

dp=[0]*12 #N은 최대 11보다 작다
dp[1]=1 # (1)
dp[2]=2 # (1,1), (2)
dp[3]=4 # (1,1,1), (1,,2), (2,1), (3)
for tc in range(1,T+1):
    N=int(input())

    # 점화식 dp[n]=dp[n-1]+dp[n-2]+dp[n-3]
    # n >=4 일때
    # n에서 n-1의 방법수에서 +1
    # n에서 n-2의 방법수에서 +2
    # n에서 n-3의 방법수에서 +3
    # 만큼 더한 만큼의 방법수 이기 때문에

    if dp[N] ==0: # 아직 구한 적 없는 정수일 경우만 구하기
        for i in range(4,N+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

    print(dp[N])