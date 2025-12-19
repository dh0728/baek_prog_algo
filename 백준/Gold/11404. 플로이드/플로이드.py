import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip()) # 도시의 개수
M = int(input().strip()) # 버스의 개수

INF = 10 ** 8
dist = [[INF] * N for _ in range(N)]

for i in range(N): # 출발지와 도착지는 같을 수 없음
    dist[i][i] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    # 같은 노선이 여러 개일 경우 최소 경로만
    if C < dist[A][B]:
        dist[A][B] = C
    
def dijkstra():
    for k in range(N):
        for i in range(N):
            if dist[i][k] == INF: # i -> k 로 못가면 패스
                continue
            ik = dist[i][k] # i -> k 까지의 비용
            for j in range(N):
                nd = ik + dist[k][j] # i -> k -> j 까지의 비용
                if nd < dist[i][j]:  # 최소 비용이면 
                    dist[i][j] = nd  # 교체
    return

def solution():

    dijkstra()

    for i in range(N):
        row = []
        for j in range(N):
            row.append("0" if dist[i][j] == INF else str(dist[i][j]))

        print(" ".join(row))

if __name__ == "__main__":
    solution()


