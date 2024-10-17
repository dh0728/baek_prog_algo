import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())

A = list(map(int,input().split()))

dp = [1]*N

for i in range(1,N): # i 현재 수의 index
    for j in range(i): # j 현재 수의 왼쪽에 있는 수
        if A[i] > A[j]:  # 왼쪽 수에서 오른쪽 보다 작은 수 중에
            dp[i] = max(dp[i],dp[j]+1) # 가장 큰수 +1이 현재 수에서의 최대 길이이다.

print(max(dp))