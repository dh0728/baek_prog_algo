import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())

dp = [[0,0,0] for _ in range(N)]

RGB= [list(map(int,input().split())) for _ in range(N)]

# 첫번째 집이 선택한 색의 비용 넣어주기
dp[0][0]=RGB[0][0]
dp[0][1]=RGB[0][1]
dp[0][2]=RGB[0][2]

# 두번째 집부터 최솟값 찾아주기
for i in range(1,N):
    # 각 RGB를 선택했을 때의 최솟값을 모두 구하기
    dp[i][0]=min(dp[i-1][1]+RGB[i][0],dp[i-1][2]+RGB[i][0])
    dp[i][1]=min(dp[i-1][0]+RGB[i][1],dp[i-1][2]+RGB[i][1])
    dp[i][2]=min(dp[i-1][0]+RGB[i][2],dp[i-1][1]+RGB[i][2])

print(min(dp[N-1])) # 마지막에 값이 제일 작은 값이 최솟값