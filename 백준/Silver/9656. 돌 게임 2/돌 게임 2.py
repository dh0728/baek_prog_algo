import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())


if N % 2:
    print("CY")
else:
    print("SK")