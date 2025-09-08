import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = 3

result = "123456780"


board = ""
x_location = 0

for _ in range(N):
    board += input().strip().replace(" ", "")

x_location = board.find("0") // 2


def inversion_count():

    inversion = 0
    lens = N * N

    for x in range(lens - 1):
        n = int( board[x])
        if n == 0 :
            continue
        for y in range(x + 1, lens):
            k = int( board[y] )
            if k == 0:          # 0은 비워진 곳이므로 패스
                continue
            if k < n:
                inversion += 1
    return inversion    

def slide_puzzle():

    inversion = inversion_count()

    if N % 2 == 1: # 홀수
        if inversion % 2 == 0:
            return True
        return False
    else:
        if x_location % 2 == 1: # x 위치가 맨아래에서 홀수 행에 있으면
            if inversion % 2 == 0:
                return True
            return False
        else:
            if inversion % 2 == 1:
                return True
            return False

dxy = [[0,1], [1,0], [0,-1], [-1,0]]

def bfs():

    # 퍼즐 상태, 이동횟수 저장 딕셔너리
    puzzle_dict = dict()
    puzzle_dict[board] = 0

    q = deque()
    q.append(board)

    while q:

        now = q.popleft()

        # 퍼즐 완성했으면
        if now == result: 
            return puzzle_dict[now] 

        loc = now.find("0")

        x = loc // N
        y = loc % N

        for xy in dxy:
            nx = x + xy[0]
            ny = y + xy[1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 퍼즐을 벗어날 경우 패스
                continue
            
            next_loc = nx * 3 + ny # 이동할 위치

            string_to_list = list(now) # 리스트로 바꾸기 (이동시킬려고)

            string_to_list[loc] , string_to_list[next_loc] = string_to_list[next_loc] , string_to_list[loc] # 위치 교환

            next = "".join(string_to_list)

            if not puzzle_dict.get(next): # 이미 전에 이동한 적이 있는 퍼즐상태이면
                q.append(next)
                puzzle_dict[next] = puzzle_dict[now] + 1


def solution():

    is_finish = slide_puzzle()
    answer = 0

    if is_finish:
        answer = bfs()
    else:
        answer = -1
    
    print(answer)

if __name__ == "__main__":
    solution()


