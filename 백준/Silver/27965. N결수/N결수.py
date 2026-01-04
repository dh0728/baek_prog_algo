import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

def solution():

    num = 0
    for i in range(1, N+1):
        d = len(str(i))
        num = (num * pow(10, d, K) + i) % K

    print(num)

    
if __name__ == "__main__":
    solution()
