import sys
input=sys.stdin.readline

N=int(input())
arr=[0]*301
for i in range(1,N+1):
    arr[i]=int(input())

dp=[0]*301 # 최대 계단 수만큼 초기화, 계단수 만큼 만들면 N이 3보다 작은 경우 인덱스에러남
dp[1]=arr[1]
dp[2]=arr[1]+arr[2]
dp[3]=max(arr[1]+arr[3],arr[2]+arr[3]) # 첫번쨰 세번째와 첫번째 두번째 계단 건넌 것 중 더 큰값 넣기

for i in range(4,N+1):
    # i-1 계단에서 올라온 경우와 i-2 계단에서 올라온 경우중 더 큰것이 들어감
    dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i]) # arr는 0부터 시작이므로 -1을 더빼줌

print(dp[N])