import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


R, C = map(int, input().split()) # R 세로  , C 가로

board = [ input().strip() for _ in range(R)]

dxy = [[0, 1],[1, 0],[0, -1],[-1, 0]]


def bit(ch):
    return 1 << (ord(ch) - 65)

def dfs(start):

    start_mark = bit(board[start[0]][start[1]])
    count = 1
    stack = [( start[0], start[1], count, start_mark)]
    

    while stack:

        x, y, cnt, mask = stack.pop()

        if cnt > count: # 더 많이 이동할 수 있는 경우를 찾으면
            count = cnt

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= R or ny < 0 or ny >= C: # 보드를 벗어나면 패스
                continue
            
            b = bit(board[nx][ny])
            if mask & b: # 이미 쓴 알파벳이면
                continue

            stack.append((nx, ny, cnt + 1, mask | b))
    return count


def solution():

    answer = dfs([0,0])
    
    print(answer)


if __name__ == "__main__":
    solution()


