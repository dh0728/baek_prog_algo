import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

arr =[list(map(int, input().split())) for _ in range(N)]
dxy = [[0,1],[1,0],[0,-1],[-1,0]]

def dfs(h):

    visited = [[0] * N for _ in range(N)]
    cnt = 1

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] > h:
                # print(f"안전구역 발견")
                stack = []
                stack.append((i,j))
                visited[i][j] = cnt

                while stack:
                    r, c = stack.pop()

                    for dx, dy in dxy:
                        nr = r + dx
                        nc = c + dy

                        # 범위를 벗어나면
                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue
                        
                        # 이미 방문한 적이 있으면
                        if visited[nr][nc] != 0:
                            continue

                        # 잠긴 지역이면
                        if arr[nr][nc] <= h:
                            continue
                        
                        stack.append((nr,nc))
                        visited[nr][nc] = cnt
                
                cnt += 1
    # for i in range(N):
        # print(*visited[i])

    return cnt - 1

max_hight = 1
res = 0

#1. 최대 높이를 찾기
for i in range(N):
    for j in range(N):
        h = arr[i][j]
        if h > max_hight:
            max_hight = h


for i in range(max_hight):
    safy_cnt = dfs(i)
    # print(f"높이:{i} 일때 안전구역수 : {safy_cnt}")

    if safy_cnt > res:
        res = safy_cnt

print(res)

