import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

def solution():

    # 상하 와 좌우를 각각 나누어서
    top_row, down_row = N, -1   # 위, 아래 
    left_col, right_col = N, -1 # 좌, 우

    for i in range(N):
        line = input().strip()
        for j, ch in enumerate(line):
            if ch == "G":
                if i < top_row:
                    top_row = i
                if i > down_row:
                    down_row = i

                if j < left_col:
                    left_col = j
                if j > right_col:
                    right_col = j

    # 이미 같은 줄에 있으면 0 처리 해야함
    min_row = 0
    min_col = 0
    if top_row == down_row:
        min_row = 0
    else:
        # 더작은 비용 찾기
        min_row  = min(down_row, N-1 - top_row) # 가장위 ->가장 아래로 보내는 비용 vs 가장 아래 -> 가장 위로 보내는 비용
    
    if left_col == right_col:
        min_col = 0
    else:
        min_col = min(right_col, N-1 - left_col) # 가장오른쪽 -> 가장 왼쪽으로 보내는 비용 vs 가장 왼쪽을 가장 오른쪽으로 보내는 비용
    
    print(min_row + min_col)
    return

if __name__ == "__main__":
    solution()

