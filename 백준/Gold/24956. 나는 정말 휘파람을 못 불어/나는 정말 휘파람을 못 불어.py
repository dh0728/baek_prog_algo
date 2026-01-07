import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
DIV = 1000000007

N = int(input().strip())
arr = input().strip()

def solution():
    w = 0
    wh = 0
    whe1 = 0
    whee = 0

    for i in range(N):

        if arr[i] == "W":
            w += 1
        elif arr[i] == "H":
            wh += w
        elif arr[i] == "E":
            new_whee = 2 * whee + whe1 # 기존 whee는 선택 or 비선택 2배 + whe1에서 E 붙여서 whee 완성
            new_whe = whe1 + wh        # wh에 E 붙여서 whe1 + 기존 whe에서 E안쓰는 경우
            whee, whe1 = new_whee, new_whe 

    print(whee % DIV)

 

if __name__ == "__main__":
    solution()
