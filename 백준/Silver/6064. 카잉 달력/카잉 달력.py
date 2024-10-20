import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

def cal_year(M,N,X,Y):
    k = X
    while k <=M*N: # 종말의 해는 m,n의 최소공배수
        if (k-X) % M == 0 and (k-Y) % N == 0: # 순서를 찾으면
            return k
        else:
            k +=M
    return -1


T= int(input())
for tc in range(1,T+1):
    M, N, X, Y =map(int,input().split())
    result=cal_year(M,N,X,Y)
    print(result)