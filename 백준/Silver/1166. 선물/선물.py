import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, L, W, H = map(int,input().split())


def solution():

    left = 0
    right = min(L, W, H)

    for _ in range(1000):

        mid = (left + right) / 2
        cnt = (L // mid) * (W // mid) * (H //mid) 

        if cnt >= N:
            left = mid
        else:
            right= mid

    print(left)
    return

if __name__ == "__main__":
    solution()


