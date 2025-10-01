import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N = int(input())

graph = [[' '] * (2 * N - 1) for _ in range(N)]

def draw(x, y, n):
    if n == 3:
        graph[x][y] = "*"
        graph[x + 1][y -1] = graph[x+ 1][y + 1] = "*"
        for i in range(-2 , 3):
            graph[x+2][y+i] = "*"
        return
    
    h = n // 2

    # 위
    draw(x,y,h)

    # 왼쪽 아래
    draw(x + h, y - h, h)

    # 오른쪽 아래
    draw(x + h, y + h, h)



def solution():
    draw(0, N - 1, N)
    for row in graph:
        print("".join(row))



if __name__ == "__main__":
    solution()


