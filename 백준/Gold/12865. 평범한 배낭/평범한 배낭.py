import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# N : 준서가 필요하다고 생각하는 물건 갯수
# K : 배낭에 넣을 수 있은 최대 무게
N, K = map(int,input().split())

def solution():

    dp = [0] * (K + 1)
    for _ in range(N):

        W , V = map(int, input().split()) # W : 물건의 무게 V : 물건의 가치

        for w in range(K, W - 1, -1):
            dp[w] = max(dp[w], dp[w- W] + V)

    print(dp[K])
                


if __name__ == "__main__":
    solution()
