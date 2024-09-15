import sys
# sys.stdin=open('input.txt')

def find_prime(n):
    end= int(n**0.5) # n을 제곱근한 숫자보다 같거나 작은 숫자만 나눠서 확인
    start=2
    while start <= end:
        if n%start ==0:
            return 0
        start+=1
    return 1
M,N=map(int,sys.stdin.readline().split())
for n in range(M,N+1):
    if n==1:
        continue
    else:
        if find_prime(n):
            print(n)