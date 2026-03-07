import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int,input().split()) # N : 동전의 종류, 동전을 합해 K의 가치를 만들고 싶음

coins = [int(input().strip()) for _ in range(N)]

coins.sort()

dp = [100001] * (K+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, K +1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[K] == 100001:
    print(-1)
else:
    print(dp[K])

