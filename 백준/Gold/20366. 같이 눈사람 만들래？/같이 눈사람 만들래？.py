import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = float('inf')

N = int(input().strip())
arr = list(map(int, input().split()))

arr.sort()


def solve():
    res = MAX

    for i in range(N):
        for j in range(i+3, N):
            left = i + 1
            right = j - 1
            while left < right:
                tmp = (arr[i] + arr[j]) - (arr[left] + arr[right])

                # 최솟값 찾으면 갱신
                if abs(tmp) < abs(res):
                    res = abs(tmp)
                
                # tmp가 0보다 작으면 (arr[i] + arr[j]) < (arr[left] + arr[right]) 이므로 
                # (arr[left] + arr[right]) 크기를 줄여야 더 최소를 찾을 수 있음
                if tmp < 0:
                    right -= 1

                # 반대의 경우도 마찬가지 늘려야 찾기 가능
                else:
                    left += 1



    return res

res = solve()

print(res)