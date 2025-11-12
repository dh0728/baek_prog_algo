import sys
#sys.stdin = open("input.txt", "r")
import math
input = sys.stdin.readline

# 한 변의 길이 구하는 함수
def cal_length(ax, ay, bx, by):
    return math.sqrt(pow((ax - bx),2) + pow((ay - by),2))

def is_oneline(Ax, Ay, Bx, By, Cx, Cy):


    cross = (Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax)
    
    if cross == 0:
        return True
    
    return False



def solution():
    Ax, Ay, Bx, By, Cx, Cy = map(int, input().split())
    
    # 만약 3점이 한 직선에 있다면
    if is_oneline(Ax, Ay, Bx, By, Cx ,Cy):
        print(-1.0)
        return
    

    len_list = [0, 0, 0]
    len_list[0] = cal_length(Ax, Ay, Bx, By)
    len_list[1] = cal_length(Bx, By, Cx, Cy)
    len_list[2] = cal_length(Ax, Ay, Cx, Cy)

    len_list.sort()
    #print(len_list)

    max_round = len_list[2] * 2 + len_list[1] * 2
    min_round = len_list[1] * 2 + len_list[0] * 2 

    result = max_round - min_round

    print(result)
    return



if __name__ == "__main__":
    solution()


