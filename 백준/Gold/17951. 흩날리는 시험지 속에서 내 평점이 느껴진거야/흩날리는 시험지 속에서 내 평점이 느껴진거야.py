import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

MAX = sum(arr)
MIN = min(arr)

def solve(left, right):
    res = 0
    while left <= right:

        mid = (left + right) // 2
        cnt = 0
        tmp = 0
        for i in range(N):
            tmp += arr[i]
            if tmp >= mid:
                tmp = 0
                cnt += 1

        # 그룹 수가 K 이상이면 mid를 더 높여야함
        # K 개가 나오더라도 최대라고 장담할 수 없음
        if cnt >= K:
            left = mid + 1
        
        else:
            right = mid - 1

    return right

res = solve(MIN, MAX)
print(res)
