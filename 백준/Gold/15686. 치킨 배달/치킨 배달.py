import sys
from itertools import combinations
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# N : 맵 크기
# M : 수익을 많이 낼 수 있는 치킨집 개수 
N, M = map(int,input().split())

# 0 : 빈칸, 1 : 집, 2: 치킨집
board = [ list(map(int , input().split())) for _ in range(N)]

houses = []
chicken = []

# 치킨집과 집 좌표 구하는 메서드
def coordinate_counting():

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 : # 집이면
                houses.append([i,j])
            elif board[i][j] == 2: # 치킨집이면
                chicken.append([i,j])

# 각 집에서 각 치킨집까지의 거리를 구하는 메서드
def calculation_distance(chicken):
    
    result = 0
    for hx, hy in houses:
        min_dis = 9999999
        for cx, cy in chicken:
           dis = abs(cx - hx) + abs(cy - hy) 
           if dis < min_dis:
               min_dis = dis
        result += min_dis
    return result



def solution():

    coordinate_counting()


    min_length = 9999999

    for chick in combinations(chicken, M):
        dis = calculation_distance(chick)
        if dis < min_length:
            min_length = dis

    print(min_length)
            
if __name__ == "__main__":
    solution()
