import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, P, Q, X, Y = map(int, input().split())

A = {}

def cal_A(n):
    if n <= 0:
        return 1
    
    if n not in A:
        A[n] = cal_A((n//P) - X) + cal_A((n//Q) - Y)
    
    return A[n] 

def solution():
    A[0] = 1

    print(cal_A(N))
    
if __name__ == "__main__":
    solution()
