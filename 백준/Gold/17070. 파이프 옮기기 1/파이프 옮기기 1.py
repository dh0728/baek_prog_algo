import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 집의 크기
N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

dp = [[[-1]*3 for _ in range(N)] for _ in range(N)]

def dfs(x, y, dir):

    if x == N - 1 and y == N - 1: # 도착했으면
        return 1
    if dp[x][y][dir] != -1:
        return dp[x][y][dir]
    
    ways = 0

    # 1) 가로 이동: 현재 가로/대각일 때만 가능, (x, y+1)이 빈칸
    if dir in (0, 2):
        ny = y + 1
        if ny < N and board[x][ny] == 0:
            ways += dfs(x, ny, 0)

    # 2) 세로 이동: 현재 세로/대각일 때만 가능, (x+1, y)이 빈칸
    if dir in (1, 2):
        nx = x + 1
        if nx < N and board[nx][y] == 0:
            ways += dfs(nx, y, 1)

    # 3) 대각 이동: 세 칸 (x,y+1), (x+1,y), (x+1,y+1)이 모두 빈칸
    nx, ny = x + 1, y + 1
    if nx < N and ny < N:
        if board[x][ny] == 0 and board[nx][y] == 0 and board[nx][ny] == 0:
            ways += dfs(nx, ny, 2)

    dp[x][y][dir] = ways
    return ways


def solution():

    if board[0][0] == 1 or board[0][1] == 1:
        print(0)
        return
    else:
        print(dfs(0,1,0))

            
if __name__ == "__main__":
    solution()


