import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


A, B = map(int, input().split())

# 소인수분해
def find(n):
    cnt = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            cnt += 1 
    if n != 1:
        cnt += 1
    
    return cnt

def solution():

    is_prime = [True] * (B + 1)
    is_prime[1] = False # 1은 소수 아님

    # 에라토스테네스의 체 알고리즘(소수 찾기)
    for i in range(2, int(math.sqrt(B)) + 1):
        if not is_prime[i]:
            continue

        for j in range(2 * i, B + 1, i):
            is_prime[j] = False

    res = 0
    for n in range(A, B+1):
        cnt = find(n)

        if is_prime[cnt]:
            res += 1

    print(res)
    return

if __name__ == "__main__":
    solution()


