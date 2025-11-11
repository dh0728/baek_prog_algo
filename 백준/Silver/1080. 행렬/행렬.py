import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def define_board(): # 행렬 초기화 함수
    board = []
    for _ in range(N):
        row = list(map(int, input().strip()))
        board.append(row)
    return board

# 행렬 숫자 교체 함수 
def change_board(x,y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if A[i][j] == 0:
                A[i][j] = 1
            else :
                A[i][j] = 0 
N, M = map(int, input().split())

# 행렬 동일하게 바꿨는지 확인한느 함수
def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    
    return True

A = define_board()
B = define_board()


def solution():

    if (N < 3 or M < 3) and A != B: # 3보다 길이짧고 서로 다르면 못바꿈
        print(-1)
        return

    result = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                change_board(i,j)
                result +=1
    if check():
        print(result)
    else:
        print(-1)
    return


if __name__ == "__main__":
    solution()


