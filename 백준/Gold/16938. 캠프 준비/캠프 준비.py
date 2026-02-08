import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N, L, R, X = map(int, input().split())
level = list(map(int, input().split()))

res = 0

for mask in range(3, 1 << N):

    problem = []
    pro_level = []

    # 문제 결정하기
    for i in range(N):
        if mask & (1 << i):
            problem.append(i)
            pro_level.append(level[i])

    # 두문제 이하이면 패스
    if len(pro_level) < 2:
        continue

    total_level = sum(pro_level)

    # L <= 난이도의 합 <= R가 아니면 패스
    if total_level < L or total_level > R:
        continue

    pro_level.sort()

    # 가장어려운 문제 - 가장 쉬운문제 < X이면 패스
    if pro_level[-1] - pro_level[0] < X:
        continue

    res += 1

print(res)