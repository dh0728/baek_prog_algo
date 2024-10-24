import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

N= int(input())
arr=list(map(int,input().split()))

dp = [N]*N
dp[0]=0

for i in range(N):
    for j in range(arr[i]+1): # j = 점프로 갈 수 있는 칸 수
        if i+j < N:
            dp[i+j]=min(dp[i+j],dp[i]+1)

if dp[N-1] < N:
    print(dp[N-1])
else:
    print(-1)