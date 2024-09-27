import sys
input = sys.stdin.readline

def p(n):
    num=1
    while n > 0:
        num *=n
        n-=1
    return num
N= int(input())

print(p(N))