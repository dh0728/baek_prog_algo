import sys
from itertools import combinations
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())


# T = 선생님, S = 학생
board = [ list(input().split()) for _ in range(N)]

dxy = [[0,1],[1,0],[0,-1],[-1,0]]

### 현재 선생님 감시망에 학생이 걸리는지 확인하는 메서드
def scaning(sx, sy):
    for dx, dy in dxy:
        n = 1
        while True:
            nx = sx + (dx * n) 
            ny = sy + (dy * n)

            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위 벗어나면 패스
                break

            if board[nx][ny] == "O": # 장애물 만나면 패스 
                break

            if board[nx][ny] == "S": # 학생 발견하면
                return False

            n += 1

    return True

def solution():

    blanks = []

    teachers = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == "X":
                blanks.append([i,j])
            elif board[i][j] == "T":
                teachers.append([i,j])

    for comb in combinations(blanks, 3):

        # 장애물 설치하기
        for x, y in comb:
            board[x][y] = 'O'

        result = True

        for tx, ty in teachers:
            if not scaning(tx, ty):
                result = False
                break
                
        if result:
            print("YES")
            return

        for x, y in comb:
            board[x][y] = "X"

    
    print("NO")


if __name__ == "__main__":
    solution()


