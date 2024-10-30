import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    # 2행 DP배열 형성
    dp = [[0] * N for _ in range(2)]


    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if N == 1: # 스티커 길이가 1일 경우
        print(max(dp[0][0], dp[1][0]))
        continue


    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if N == 2: # 스티커 길이가 2일 경우
        print(max(dp[0][1], dp[1][1]))
        continue

    # 스티커 길이가 3이상일 경우
    for i in range(2, N):
        # 마지막 열은 무조건 둘중 하나는 더해진다.
        # i-1열을 건너뛰는 경우가 더 클수도 있기 떄문에 건너뛴 경우와 아닌 경우
        # 둘중 더 큰값을 dp에 넣기
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + arr[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + arr[1][i]

    print(max(dp[0][-1], dp[1][-1]))