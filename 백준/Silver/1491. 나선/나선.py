import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def solution():

    N, M = map(int, input().split())  # N: x(가로), M: y(세로)
    L, R = 0, N - 1
    B, T = 0, M - 1

    x, y = 0, 0
    d = 0  # 0:E, 1:N, 2:W, 3:S

    while True:
        if d == 0:  # E
            x, y = R, B
            B += 1
        elif d == 1:  # N
            x, y = R, T
            R -= 1
        elif d == 2:  # W
            x, y = L, T
            T -= 1
        else:  # S
            x, y = L, B
            L += 1

        # 다음 이동 전에 남은 영역이 없으면 종료
        if L > R or B > T:
            break

        d = (d + 1) % 4

    print(x, y)
    
    
if __name__ == "__main__":
    solution()

