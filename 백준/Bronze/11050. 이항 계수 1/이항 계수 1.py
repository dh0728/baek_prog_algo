def bino_coefficient(n, k):
    if k == 0 or n == k:
        return 1
    return bino_coefficient(n-1, k) + bino_coefficient(n-1, k-1)

N,K=map(int,input().split())
result=bino_coefficient(N,K)
print(result)