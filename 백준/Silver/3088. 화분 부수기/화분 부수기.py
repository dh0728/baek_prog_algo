import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

flower = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

dp = [0 for _ in range(10**6 + 1)]

for a, b, c in flower:
    if not dp[a] and not dp[b] and not dp[c]:
        cnt += 1
    dp[a], dp[b], dp[c] = 1, 1, 1
print(cnt)
    