import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, S = map(int,input().split())
seq = list(map(int, input().split()))

def solution():
    res = 0

    for m in range(1, 1<< N):
        total = 0
        for i in range(N):
            if m & (1 << i):
                total += seq[i]
        if total == S:
            res +=1

    print(res)
    return

if __name__ == "__main__":
    solution()


