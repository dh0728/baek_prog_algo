import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
reversed_arr = arr[::-1]

def solution():
    
    dp = [1] * N
    reversed_dp = [1] * N

    for i in range(1, N):
        for j in range(i): # 현재 수의 왼쪽에 있는 수
            if arr[i] > arr[j]: # 왼쪽 수들 중에서 오른쪽보다 작은 수중에서
                dp[i] = max(dp[i], dp[j] + 1) #가장 큰수 +1이 현재 수에서의 최대 길이
            if reversed_arr[i] > reversed_arr[j]:
                reversed_dp[i] = max(reversed_dp[i], reversed_dp[j] + 1)
                
    res = [(dp[i] + reversed_dp[N-i-1] - 1) for i in range(N)]

    print(max(res))


if __name__ == "__main__":
    solution()