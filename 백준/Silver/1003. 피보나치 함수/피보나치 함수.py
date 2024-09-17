import sys
input=sys.stdin.readline
# sys.stdin=open('input.txt')

def fibonacci(n):
    for i in range(3, n+1):
        d[i]=d[i-1]+ d[i-2] # 피보나치 원리

T=int(input())
for tc in range(1,1+T):
    d=[0]*41 # DP 리스트 초기화
    d[1]=1
    d[2]=1
    N=int(input())
    fibonacci(N)
    if N==0:
        print(1,0)
    else:
        print(d[N-1],d[N])