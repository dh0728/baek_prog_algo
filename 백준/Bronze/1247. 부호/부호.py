import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

for tc in range(3):
    S = 0
    N=int(input())
    for _ in range(N):
        S += int(input())

    if S ==0:
        print(0)
    elif S > 0:
        print('+')
    else:
        print('-')








