import sys
import math
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

A, B = map(int, input().split())

size = int(math.sqrt(B) + 1) 

primes = [i for i in range(size)]


def isPrime():
    
    for i in range(2, size):
        if primes[i] == 0:
            continue
        for j in range(2*i , size ,i):
            primes[j] = 0

def solution():
    isPrime()
    cnt = 0
    for i in range(2, size):
        if primes[i] != 0: # 소수이면
            tmp = primes[i] * primes[i]
            while tmp <= B:
                if tmp >= A:
                    cnt += 1
                tmp *= primes[i]
    
    print(cnt)

if __name__ == "__main__":
    solution()

