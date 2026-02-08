import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = float("inf")

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = INF

# 절반만 탐색 
for mask in range(1, (1<<N)//2):

    start_team = []
    link_team = []

    for i in range(N):
        if mask & (1 << i):
            start_team.append(i)
        else:
            link_team.append(i)

    # 두팀 모두 1명 이상은 있어야함
    if len(start_team) == 0 or len(link_team) == 0:
        continue


    start_power = 0
    link_power = 0

    # 스타트 팀 능력치
    for i in range(len(start_team)):
        for j in range(i+1, len(start_team)):
            a = start_team[i]
            b = start_team[j]
            start_power += arr[a][b] + arr[b][a]

    # 링크 팀 능력치
    for i in range(len(link_team)):
        for j in range(i+1, len(link_team)):
            a = link_team[i]
            b = link_team[j]
            link_power += arr[a][b] + arr[b][a]

    ans = min(ans, abs(start_power - link_power))

print(ans)