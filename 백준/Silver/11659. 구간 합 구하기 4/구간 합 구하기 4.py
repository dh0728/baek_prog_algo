import sys
input=sys.stdin.readline


# 수열 만드는 함수
N, M = map(int,input().split())
arr=list(map(int,input().split()))

arr_sum=[]
sum_n=0
for i in range(N): # 누적해서 값이 더해지는 리스트 만들기
    sum_n+=arr[i]
    arr_sum.append(sum_n)

for _ in range(M):
    i, j= map(int,input().split())
    if i-2 < 0:
        print(arr_sum[j - 1]) # 처음부터 j 번까지의 합일경우
    else:
        print(arr_sum[j-1]-arr_sum[i-2]) # i 부터 j 번까지의 합일 경우