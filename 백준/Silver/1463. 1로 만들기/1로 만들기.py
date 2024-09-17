import sys
input=sys.stdin.readline

N=int(input())
dp=[0]*(N+1)

for i in range(2,N+1): # 2일때부터 시작해서 횟수 구하기
    dp[i]=dp[i-1]+1 # 1을 뺐을 때의 연산횟수
    if i % 2 == 0: # 2로 나누어 진다면
        if dp[i//2]+1 < dp[i]: # 2로 나누었을 때와 1을 뺐을 때의 연산횟수 비교
            dp[i]=dp[i//2]+1   # 2로 나눈게 더 작으면 교체
    if i % 3 == 0:  # 3로 나누어 진다면
        if dp[i//3]+1 < dp[i]: # 3으로 나누었을 때 연산횟수와 나머지 비교
            dp[i]=dp[i//3]+1   # 3으로 나누었을 때가 더 작으면 교체

print(dp[N])