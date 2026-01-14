import sys
from collections import defaultdict
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

S = input().strip()
N = len(S)

def is_pal(s):
    return s == s[::-1]

def solution():
    
    for i in range(N):
        if is_pal(S[i:]):
            print(N + i)
            break
    return

if __name__ == "__main__":
    solution()