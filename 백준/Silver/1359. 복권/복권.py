import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N, M, K = list(map(int, input().split()))
numbers = [i for i in range(1, N+1)]

def solution():

    comb = math.comb(N, M)
    win = 0

    for i in range(K, M+1):
        win += math.comb(M, i) * math.comb(N- M, M - i)
    print(win/comb)

if __name__ == "__main__":
    solution()