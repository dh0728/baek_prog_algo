import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip()) # N : 판자의 개수

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

board.sort()

def greedy(merged):
    curL, curR = merged[0]
    reach = 2 * curR - curL
    idx = 1
    res = curR
    
    while True:
        best_next_reach = reach  
        best_board = None
        best_end = curR
        
        # 도달가능한 판자들까지만 반복
        while idx < len(merged) and merged[idx][0] <= reach:
            L, R = merged[idx]
            best_end = max(best_end, R)
            
            # 현재판자의 다음 도달거리
            next_reach = 2 * R - L
            if next_reach > best_next_reach: # 최대 도달거리가 갱신
                best_next_reach = next_reach
                best_board = (L, R)          # 최대 도달가능한 판자
            idx +=1

        res = max(res, best_end)

        # reach를 더 못 키우면, 현재까지 가능한 최대 끝점이 정답
        if best_board is None:
            print(res)
            return
        
        curL, curR = best_board
        reach = best_next_reach

    return


def solution():
    
    merged = []
    left, right = board[0]

    # 새로운 판자가 서로 이어지면 병합하기
    for l, r in board[1:]:
        if l <= right: 
            if r > right:
                right = r
        else:
            merged.append((left, right))
            left = l
            right = r
    merged.append((left, right))

    greedy(merged)    
    return
    
    
if __name__ == "__main__":
    solution()

