import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

# 비트마스킹을 이용해서 모든 경우의 수를 계산
# 1:은 가로 숫자 0:세로 숫자를 의미
def solution():
    res = 0
    for mask in range(1 << (N*M)):
        total = 0
        # 가로합 계산
        for row in range(N):
            row_sum = 0
            for col in range(M):
                idx = row * M + col
                if mask & (1 << idx) != 0: # 가로 숫자일 경우 
                    row_sum = row_sum * 10 + arr[row][col]
                else:
                    total += row_sum # 세로 숫자일 경우
                    row_sum = 0
            total += row_sum
        
        
        # 세로합 계산
        for col in range(M):
            col_sum = 0
            for row in range(N):
                idx = row * M + col
                if mask & (1 << idx) == 0: # 세로 숫자일 경우
                    col_sum = col_sum * 10 + arr[row][col]
                else:
                    total += col_sum    # 가로 숫자일 경우
                    col_sum = 0
            total += col_sum

        res = max(total, res)
    return res

print(solution())

