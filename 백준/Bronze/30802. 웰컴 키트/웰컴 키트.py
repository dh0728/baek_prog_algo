N=int(input())
arr= list(map(int,input().split())) #S, M, L , XL , XXL , XXXL
T , P =map(int,input().split())

cnt=0
for a in arr:
    if a/T > a//T:
        cnt+=a//T+1
    else:
        cnt+=a//T

pen_set=N//P
pen_cnt=N%P
print(cnt)
print(pen_set, pen_cnt)