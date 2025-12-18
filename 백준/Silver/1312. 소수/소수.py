import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

A, B, N = map(int, input().split())
def solution():
    global A

    for _ in range(N):
        A = (A%B) * 10
    print(A//B)


if __name__ == "__main__":
    solution()


