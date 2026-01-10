import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split()) # N: 체스판의 크기, K: 흑색 퀸의 수 
R, C = map(int, input().split()) # 백색 킹의 위치

rows = []
cols = []
diag1 = []
diag2 = []

for _ in range(K): 
    X, Y = map(int, input().split()) 
    rows.append(X)
    cols.append(Y)
    diag1.append(X-Y)
    diag2.append(X+Y)

def attack(r, c):
    diag1_num = r - c
    diag2_num = r + c

    # 공격 받을 수 있는 공이면 True
    if (r in rows) or (c in cols) or (diag1_num in diag1) or (diag2_num in diag2):
        return True
    return False

def solution():
    dxy = [[-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1]]
 

    current_attacked = attack(R,C) # False가 안전한거
    move_attacked = True

    for dx, dy in dxy:
        nx = R + dx
        ny = C + dy

        # 범위 벗어나면 패스
        if nx < 1 or nx > N or ny < 1 or ny > N:
            continue

        if not attack(nx, ny): # 안전한 곳을 찾으면
            move_attacked = False
            break
        
    if current_attacked: # 시작위치가 공격당할 수 있으면
        if move_attacked: # 체크 or 체크메이트
            print("CHECKMATE")
        else:
            print("CHECK")
    else:
        if move_attacked: # 스타일메이트 or NONE
            print("STALEMATE")
        else:
            print("NONE")

    return

if __name__ == "__main__":
    solution()

