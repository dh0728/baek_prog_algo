import sys
import collections
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

def solution():

    for _ in range(T):
        a, b = map(int,input().split())
        print("yes")
        
if __name__ == "__main__":
    solution()


