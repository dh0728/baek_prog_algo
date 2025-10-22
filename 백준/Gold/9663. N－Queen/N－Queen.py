import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
row = [0] * N
ans = 0

def is_promising(x):
    rx = row[x]
    for i in range(x):
        diff = rx - row[i]
        if diff == 0 or diff == (x - i) or diff == -(x - i):
            return False
        
    return True

def n_queens(x):
    global ans 
    if x == N:
        ans += 1
        return

    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)
                
def solution():
    n_queens(0)
    print(ans)

if __name__ == "__main__":
    solution()


