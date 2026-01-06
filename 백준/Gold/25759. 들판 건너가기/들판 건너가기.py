import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("-inf")

N = int(input().strip())
arr = [0] + list(map(int,input().split()))


def solution():
    dp = [INF for _ in range(101)] # i번째 idx에서 꽃을 골랐을 때 가능한 아룸다음의 최댓값
    dp[arr[1]] = 0
    for i in range(2, N+1):
        for j in range(1, 101): # j = 이전 단계에서 선택한 마지막 꽃의 아룸다움 값(j는 arr의 인덱스 아님 X)
            if dp[j] != INF:
                dp[arr[i]] = max(dp[arr[i]], dp[j] + (arr[i] - j) ** 2) # 현재 꽃을 선택 X vs 이전 마지막 값이 j인 꽃다발 뒤에 현재 꽃(arr[i])을 붙이는 경우
    print(max(dp))

if __name__ == "__main__":
    solution()
