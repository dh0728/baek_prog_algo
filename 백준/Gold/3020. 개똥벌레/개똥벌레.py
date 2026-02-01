import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, H = map(int, input().split()) # N:길이, H:높이

up = [0] * (H+2)
down = [0] * (H+2)

def solution():

    for _ in range(N//2):
        d = int(input().strip())
        u = H - int(input().strip()) + 1
        down[d] +=1
        up[u] += 1
    
    for i in range(1, H+1):   # 높이 i 이하 석순 개수로 누적합
        down[i] += down[i-1]

    for i in range(H, 0, -1): # 높이 i 이상 종유석 개수로 누적합
        up[i] += up[i+1]

    min = N
    cnt = 0
    for i in range(1, H+1):

        # 높이 i 선을 통과하는 석순 개수 - 높이 i 선을 통과하는 종유석 개수
        dif = (down[H] - down[i-1]) + (up[1] - up[i+1]) 
        if dif < min:
            min = dif
            cnt = 1
        elif dif == min:
            cnt +=1
    print(f"{min} {cnt}")
    
if __name__ == "__main__":
    solution()