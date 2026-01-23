import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

def solution():

    i = N // 5
    n = N
    cnt = 0

    while i >= 0:
        cnt = i
        temp = n - (i * 5)

        if temp % 2 == 1:
            # 거술러 줄수 x
            i -= 1
        else:
            # 거슬러 줄수 O
            cnt += temp // 2
            print(cnt)
            return

    print(-1)
    return


if __name__ == "__main__":
    solution()

