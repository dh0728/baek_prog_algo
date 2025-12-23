import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, P, Q = map(int, input().split()) 

A = {}

def cal_A(n):
    if n not in A:
        A[n] = cal_A(n//P) + cal_A(n//Q)
    return A[n] 

def solution():
    A[0] = 1

    print(cal_A(N))
    
if __name__ == "__main__":
    solution()
