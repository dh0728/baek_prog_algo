import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited= [False for _ in range(N)]
visited[K] = True

def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
  

def dfs(curr, cost, cnt):
    global res
    if N == cnt:
        res = min(res, cost)
        return
    
    for next in range(N):
        # 이미 방문했으면 패스
        if visited[next]:
            continue

        visited[next] = True
        dfs(next, cost+arr[curr][next], cnt+1)
        visited[next] = False


res = float("INF")
floyd_warshall()
dfs(K,0,1)
print(res)
