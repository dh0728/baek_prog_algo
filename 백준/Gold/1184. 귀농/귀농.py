import sys
from collections import defaultdict
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

presum = [[0] * (N +1) for _ in range(N+1)] # presum[i][j] = arr[0][0] ~ arr[i-1][j-1]

# 누적합 계산
# presum[i-1][j-1]을 빼는 이유 : 누적합을 구하는 과정에서 presum[i-1][j-1] 부분이 두번 더해지기 때문에
for i in range(1,N +1):
    for j in range(1, N+1):
        presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + arr[i-1][j-1]

def get_prefix_sum(sx, sy, ex, ey):
    return (presum[ey][ex] - presum[sy-1][ex] - presum[ey][sx-1] + presum[sy-1][sx-1])  #  전체 - 위쪽 - 왼쪽 + 겹친 영역


def solution():
    res = 0

    for divy in range(1, N):
        for divx in range(1,N):

            # Case 1 : 왼쪽 위 - 오른쪽 아래 가 서로 같을 경우
            dd = defaultdict(int)

            # 왼쪽 위 사각형: (1,1) ~ (divx , divy)
            # 이 안에서 "오른쪽 아래 모서리가 (divx,divy)" 인 직사각형들을 열거
            for i in range(1, divy+1):
                for j in range(1, divx+1):
                    # (j, i) ~ (divx, divy)
                    dd[get_prefix_sum(j, i, divx, divy)] += 1

            # 오른쪽 아래 사각형: (divx+1, divy+1) ~ (n,n)
            # 여기서 "왼쪽 위 모서리가 (divx+1, divy+1)" 인 직사각형들
            for i in range(divy+1, N+1):
                for j in range(divx+1, N+1):
                    # (divx+1, divy+1) ~ (j, x)
                    res += dd[get_prefix_sum(divx+1, divy+1, j, i)]

            # Case 2 : 오른쪽 위 - 왼쪽 아래 가 서로 같을 경우
            dd = defaultdict(int)

            # 오른쪽 위 사각형: (divx+1, 1) ~ (n, divy)
            # 이 안에서 "왼쪽 아래 모서리가 (divx+1,divy)" 인 직사각형
            for i in range(1, divy+1):
                for j in range(divx+1, N+1):
                     # (divx+1, i) ~ (j,divy)
                    dd[get_prefix_sum(divx+1, i, j, divy)] += 1

             # 왼쪽 아래 사각형: (1, divy+1) ~ (divx, n)
             # 이 안에서 "오른쪽 위 모서리가 (divx,divy+1)" 인 직사각형
            for i in range(divy+1, N+1):
                for j in range(1, divx+1):
                    # (j,divy+1) ~ (divx,i)
                    res += dd[get_prefix_sum(j, divy+1, divx, i)]

    print(res)    
    return

if __name__ == "__main__":
    solution()

