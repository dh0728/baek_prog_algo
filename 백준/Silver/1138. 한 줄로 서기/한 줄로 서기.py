import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
lines = [0] * N
    

def solution():

    for i, n in enumerate(people):
        temp = n
        for j in range(N):
            if temp == 0 and lines[j] == 0:
                lines[j] = i + 1
                break
            if lines[j] == 0:
                temp -= 1

    for n in lines:
        print(n, end= " ")
    return

if __name__ == "__main__":
    solution()


