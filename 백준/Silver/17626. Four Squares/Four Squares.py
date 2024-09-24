import sys
input=sys.stdin.readline


def five_squares(n):
    dp=[0]*(n+1)
    num=1

    # 제곱한 값들은 모드 cnt가 1이니 바로 넣어주기
    while num**2 <= n:
        dp[num**2]=1
        num+=1
        
    if dp[n]: # 1개로 만들수 있으면 바로 리턴
        return dp[n]

    for i in range(2,n+1):
        if dp[i]: # 이미 최소개수가 카운팅 된 자연수면 패스
            continue
        j=1
        while j**2 <= i:
            if dp[i]==0: # 제곱수의 개수를 구한 적없는 수라면
                dp[i]= dp[j**2] + dp[i-j**2]
            else:   # 전에 제곱수 개수와 다음 제곱수 개수와 비교후 더 작은거 넣기
                dp[i]= min(dp[i], dp[j**2] + dp[i-j**2])
            j +=1
    return dp[n]

N=int(input())
print(five_squares(N))